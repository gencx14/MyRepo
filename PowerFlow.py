import numpy as np
from Bus import Bus
from System import System
import cmath
class PowerFlow:
    def __init__(self, ybus, system: System):
        self.tolerance = 0.00001
        self.system = system
        self.ybus = ybus
        self.plength = None
        self.qlength = None
        self.vlength = None
        self.delta_length = None
        self.y =None
        self.x = None
        self.f_x = None
        self.p_x = None
        self.q_x = None
        self.ybusarr = None
        self.xbusarr = None
        self.step1_y_array()
        self.step2_x_array_flatstart()
        self.step3_find_fx()    # still need to check math but looks right so far
        self.step4_find_delta_y()
        #  fill y for power equation from bus information

    #finds the y... THIS WORKS AS EXPECTED
    def step1_y_array(self):
        # find y array which contains starting power values but make sure that you are using the bus objects
        # 1. create a vertical array of zeros for our P values
        Ptemp = np.zeros((len(self.system.buses) - Bus.slackCount, 1))
        # 2.  create a vertical array of zeros for our P values
        Qtemp = np.zeros((len(self.system.buses) - Bus.slackCount, 1))
        # 3. create an array of the buses objects except the ones that are voltage controlled and create the P&Q arrays
        i = 0
        busarr = np.zeros(len(self.system.buses), dtype=object)
        for bus in self.system.buses:
            if self.system.buses[bus].type == "Slack":
                continue
            # busarr was added to be sure that we are editing the correct bus in final calculations
            busarr[i] = self.system.buses[bus]
            Ptemp[i] = self.system.buses[bus].pk
            Qtemp[i] = self.system.buses[bus].qk
            i += 1
        #trim excess storage from the matrix
        self.ybusarr = np.trim_zeros(busarr)
        self.plength = len(Ptemp)
        self.qlength = len(Qtemp)


        # 3. concatenate the arrays
        ytemp = np.zeros(((len(self.system.buses) - Bus.slackCount)* 2, 1))
        ytemp = np.concatenate((Ptemp, Qtemp))

        self.y = ytemp

    #finds the x
    def step2_x_array_flatstart(self):
        #  find x array which contains flat start voltage and
        # 1. create a vertical array of zeros for our delta values (voltage angles), flat start phase angle = 0 degrees
        delta_temp = np.zeros((self.plength, 1))
        # 2. create a vertical array of ones for our voltage magnitude values for our flat start (mag = 1.0 for all)
        volt_temp = np.zeros((self.plength, 1))
        busarr = np.zeros(len(self.system.buses), dtype=object)
        i = 0
        #  find slack voltages (will almost always be 1.0 and 0 degrees)
        for bus in self.system.buses:
            if self.system.buses[bus].type == "Slack":
                slackvoltage = self.system.buses[bus].vk
                slackdelta = self.system.buses[bus].delta1
                break

        # fill voltage and deltas array
        for bus in self.system.buses:
            if self.system.buses[bus].type == "Slack":
                continue
            elif self.system.buses[bus].type == "VC":
                volt_temp[i] = self.system.buses[bus].vk
                delta_temp[i] = self.system.buses[bus].delta1
            else:
                volt_temp[i] = slackvoltage
                delta_temp[i] = slackdelta
            busarr[i] = self.system.buses[bus]
            i += 1

        self.vlength = len(volt_temp)
        self.delta_length = len(volt_temp)

        self.xbusarr = np.trim_zeros(busarr)
        # 3. concatenate the arrays
        self.x = np.zeros((len(delta_temp) + len(volt_temp), 1))
        self.x = np.concatenate((delta_temp, volt_temp))

    # finds the P(x) value
    def step3_find_fx(self):
        self.p_x = np.zeros((self.plength, 1))
        self.q_x = np.zeros((self.plength, 1))
        for k in range(self.plength):
            for n in range(self.plength):
                # Compute active power flow
                self.p_x[k] += self.x[k + self.plength] * abs(self.ybus[k][n]) * self.x[n + self.plength] * np.cos(np.deg2rad(self.x[k] - self.x[n] - cmath.phase(self.ybus[k][n])))

                # Compute reactive power flow
                self.q_x[k] += self.x[k + self.plength] * abs(self.ybus[k][n]) * self.x[n + self.plength] * np.sin(np.deg2rad(self.x[k] - self.x[n] - cmath.phase(self.ybus[k][n])))
        self.f_x = np.zeros(len(self.p_x) + len(self.q_x))
        self.f_x = np.concatenate((self.p_x, self.q_x))

    # returns the change in power
    def step4_find_delta_y(self):
        delta_p = np.zeros((len(self.p_x), 1))
        delta_y = np.zeros((len(self.f_x), 1))
        delta_q = np.zeros((len(self.q_x), 1))
        for k in range(len(self.f_x)):
            delta_y[k] = self.y[k] - self.f_x[k]
        for k in range(len(self.p_x)):
            delta_p[k] = self.y[k] - self.p_x[k]
        for k in range(len(self.q_x)):
            delta_q[k] = self.y[k + self.plength] - self.q_x[k]

'''
    # find the jacobian
    def find_jacob(self):
            for row in element.buses:
                for col in element.buses:
                    index_row = self.system.buses[row].index
                    index_col = self.system.buses[col].index

                    self.J1[index_row, index_col] = self.p_x[index_row, 1] * self.system.ybus[index_row, index_col]

    def calc_J1(self):
        for k in range(self.plength):
            for n in range(self.plength):
                if k == n:
                    self.J1[k][n] = -1 * (self.q_x[k] - (self.x[k + self.plength] * abs(self.ybus[k][n]) * self.x[n + self.plength] * np.sin(np.deg2rad(self.x[k]) - np.deg2rad(self.x[n]) - cmath.phase(self.ybus[k][n]))))
                else:
                    self.J1[k][n] = self.x[k + self.plength] * abs(self.ybus[k][n]) * self.x[n + self.plength] * np.sin(
                        np.deg2rad(self.x[k]) - np.deg2rad(self.x[n]) - cmath.phase(self.ybus[k][n]))

    def calc_J2(self):
        temp = 0
        for k in range(self.plength):
            for n in range(self.plength):
                t
                if k == n:
                    self.J2[k][n] = self.x[k + self.plength] * abs(self.ybus[k][n]) * cmath.cos(cmath.phase(self.ybus[k][n]))






         J1_df = pd.DataFrame()
        J1_df.loc[self.ybusarr[k].index, self.ybusarr[k].index] =
        J1_df.loc[self.ybusarr[k].index, self.ybusarr[n].index] = self.x[k + self.plength] * abs(self.ybus[k][n]) * self.x[n + self.plength] * np.sin(np.rad2deg(self.x[k]) - np.rad2deg(self.x[n]) - np.rad2deg(cmath.phase(self.ybus[k][n])))
        J1_df.loc[self.ybusarr[n].index, self.ybusarr[k].index] = self.x[n + self.plength] * abs(self.ybus[n][k]) * self.x[k + self.plength] * np.sin(np.rad2deg(self.x[n]) - np.rad2deg(self.x[k]) - np.rad2deg(cmath.phase(self.ybus[n][k])))
        J1_df.loc[self.ybusarr[n], self.ybusarr[n]] =
        ##check to see if this saves y as a variable
        self.J1 = J1_df 

    def calc_J2(self, k, n):
        J2_df = pd.DataFrame()
        J2_df.loc[self.ybusarr[k].index, self.ybusarr[k].index] =
        J2_df.loc[self.ybusarr[k].index, self.ybusarr[n].index] = self.x[k + self.plength] * abs(self.ybus[k][n]) * np.cos(np.rad2deg(self.x[k]) - np.rad2deg(self.x[n]) - np.rad2deg(cmath.phase(self.ybus[k][n])))
        J2_df.loc[self.ybusarr[n].index, self.ybusarr[k].index] = self.x[n + self.plength] * abs(self.ybus[n][k]) * np.cos(np.rad2deg(self.x[n]) - np.rad2deg(self.x[k]) - np.rad2deg(cmath.phase(self.ybus[n][k])))
        J2_df.loc[self.ybusarr[n], self.ybusarr[n]] =
        ##check to see if this saves y as a variable
        self.J2 = J2_df

    def calc_J3(self, k, n):
        J3_df = pd.DataFrame()
        J3_df.loc[self.ybusarr[k].index, self.ybusarr[n].index] =
        J3_df.loc[self.ybusarr[k].index, self.ybusarr[k].index] = -1 * self.x[k + self.plength] * abs(self.ybus[k][n]) * self.x[n + self.plength] * np.cos(np.rad2deg(self.x[k]) - np.rad2deg(self.x[n]) - np.rad2deg(cmath.phase(self.ybus[k][n])))
        J3_df.loc[self.ybusarr[n].index, self.ybusarr[k].index] = -1 * self.x[n + self.plength] * abs(self.ybus[n][k]) * self.x[k + self.plength] * np.sin(np.rad2deg(self.x[n]) - np.rad2deg(self.x[k]) - np.rad2deg(cmath.phase(self.ybus[n][k])))
        J3_df.loc[self.ybusarr[n], self.ybusarr[n]] =
        ##check to see if this saves y as a variable
        self.J3 = J3_df

    def calc_J4(self, k, n):                    #IF THIS ISNT WORKING CHECK YOUR USE OF rad2deg function... should prob only be on outside!
        J4_df = pd.DataFrame()
        J4_df.loc[self.ybusarr[k].index, self.ybusarr[k].index] =
        J4_df.loc[self.ybusarr[k].index, self.ybusarr[n].index] = self.x[k + self.plength] * abs(self.ybus[k][n]) * np.sin(np.rad2deg(self.x[k]) - np.rad2deg(self.x[n]) - np.rad2deg(cmath.phase(self.ybus[k][n])))
        J4_df.loc[self.ybusarr[n].index, self.ybusarr[k].index] = self.x[n + self.plength] * abs(self.ybus[n][k]) * np.sin(np.rad2deg(self.x[n]) - np.rad2deg(self.x[k]) - np.rad2deg(cmath.phase(self.ybus[n][k])))
        J4_df.loc[self.ybusarr[n], self.ybusarr[n]] =
        ##check to see if this saves y as a variable
        self.J4 = J4_df





        # vector of every P, Q

        #find pk = p - px
'''
