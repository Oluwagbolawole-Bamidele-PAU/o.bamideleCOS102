from scipy.optmize import fsovle
def cubic_eq(x,a,b,c,d):
    return a*x**3 + b*x**2  + c*x  + d

#Get user input
a, b, c, d = [float(input(f"Enter coeffiencient {var}: ")) for var in ["a","b","c","d"]]

initail_gusses = [0,1,-1]
