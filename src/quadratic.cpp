// #include <iostream>
#include <math.h>
#include <boost/python.hpp>vc
// #include "quadratic.h"

double temp(double a, double b, double c){
    double inside = pow(b, 2) - (4*a*c);
    double sol1 = (-b+sqrt(inside))/(2*a);
    return sol1;
}