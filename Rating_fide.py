def calculo_fide(pontos, num_partidas, rating_oponentes):

    K = 40 
    if num_partidas >= 30:
        K = 20 
    
    soma_oponentes = sum(rating_oponentes)
    rating_oponentes_medio = soma_oponentes / num_partidas
    
    rating = pontos + K * (rating_oponentes_medio - 2000)
    return rating