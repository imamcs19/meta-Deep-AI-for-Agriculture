/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package ptvpso;

/**
 *
 * @author Core_i5
 */
public class Parameter {
    public static int SWARM_SIZE;
    public static int MAX_ITERATION;
    public static int PROBLEM_DIMENSION;
    public static double C1f;
    public static double C1i;
    public static double C2f;
    public static double C2i;
    public static double W_MAX;
    public static double W_MIN;
    public static double V0;
    public static double K;
    
    public static int getSWARM_SIZE() {
        return SWARM_SIZE;
    }

    public static void setSWARM_SIZE(int SWARM_SIZE) {
        Parameter.SWARM_SIZE = SWARM_SIZE;
    }

    public static int getMAX_ITERATION() {
        return MAX_ITERATION;
    }

    public static void setMAX_ITERATION(int MAX_ITERATION) {
        Parameter.MAX_ITERATION = MAX_ITERATION;
    }

    public static int getPROBLEM_DIMENSION() {
        return PROBLEM_DIMENSION = 12;
    }

    public static double getC1f() {
        return C1f;
    }

    public static void setC1f(double C1f) {
        Parameter.C1f = C1f;
    }

    public static double getC1i() {
        return C1i;
    }

    public static void setC1i(double C1i) {
        Parameter.C1i = C1i;
    }

    public static double getC2f() {
        return C2f;
    }

    public static void setC2f(double C2f) {
        Parameter.C2f = C2f;
    }

    public static double getC2i() {
        return C2i;
    }

    public static void setC2i(double C2i) {
        Parameter.C2i = C2i;
    }

    public static double getW_MAX() {
        return W_MAX;
    }

    public static void setW_MAX(double W_MAX) {
        Parameter.W_MAX = W_MAX;
    }

    public static double getW_MIN() {
        return W_MIN;
    }

    public static void setW_MIN(double W_MIN) {
        Parameter.W_MIN = W_MIN;
    }

    public static double getV0() {
        return V0 = 0;
    }
    
    public static void setK(double K) {
        Parameter.K = K;
    }

    public static double getK() {
        return K;
    }
    
    
}
