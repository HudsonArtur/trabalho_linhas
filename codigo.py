import math

def resistencia_por_metro_coaxial(a, b, muRelativo, sigmaC, frequencia):
    mu = muRelativo * 4 * math.pi * 10**-7
    # Calculo da resistencia por metro
    
    R = (1/a + 1/b) * 1/2*math.pi * (math.sqrt(math.pi * frequencia * mu)/sigmaC)

    return R

def resistencia_por_metro_bifilar(a, muRelativo, sigmaC, frequencia):
    mu = muRelativo * 4 * math.pi * 10**-7

    # Calculo da resistencia por metro
    
    R = (1/a * (math.sqrt(frequencia * mu)/sigmaC))

    return R

def indutancia_por_metro_coaxial(a, b, muRelativo):
    mu = muRelativo * 4 * math.pi * 10**-7
    
    # Calculo da indutancia por metro
    
    L = (mu/2*math.pi) * math.log(b/a)

    return L

def indutancia_por_metro_bifilar(a, d, muRelativo):
    mu = muRelativo * 4 * math.pi * 10**-7
    
    # Calculo da indutancia por metro
    
    L = (mu/math.pi) * math.cosh**-1(d/2*a)

    return L

def condutancia_por_metro_coaxial(a, b, sigmaD):
    
    # Calculo da condutancia por metro
    
    G = ((2*math.pi * sigmaD) / math.log(b/a))

    return G

def condutancia_por_metro_bifilar(a, d, sigmaD):
    
    # Calculo da condutancia por metro
    
    G = ((math.pi * sigmaD) / math.cosh**-1(d/2*a))

    return G

def capacitancia_por_metro_coaxial(a, b, epsilonRelativo):
    epsilon = epsilonRelativo * 8.854187817 * 10**-12
    
    # Calculo da capacitancia por metro
    
    C = (2*math.pi*epsilon) / math.log(b/a)

    return C

def capacitancia_por_metro_bifilar(a, d, epsilonRelativo):
    epsilon = epsilonRelativo * 8.854187817 * 10**-12
    
    # Calculo da capacitancia por metro
    
    C = (math.pi*epsilon) / math.cosh**-1(d/2*a)

    return C