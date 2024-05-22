def estimar_tempo_viagem(distancia, velocidade_media):
    tempo = distancia/velocidade_media
    return tempo

distancia = 200
velocidade_media = 60
tempo_estimado = estimar_tempo_viagem(distancia, velocidade_media)
print("para uma viagem de {} km e velocidade média de {} km, o tempo estimado é de {}".format(distancia,velocidade_media,tempo_estimado))