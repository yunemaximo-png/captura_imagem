import cv2


def capturar_e_salvar():

    webcam = cv2.VideoCapture(0)

    if not webcam.isOpened():
            print("Erro: Não foi possível acessar a webcam.")
            return # early return

    # Configuração da fonte do texto
    fonte = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX                  
    escala = 0.6
    cor_texto = (255, 255, 255)
    espessura = 1

    print("[ESPAÇO] Capturar e salvar uma foto")
    print("[ESCAPE] Sair")

    while True: # do-while
          status, frame = webcam.read()

          if not status:
                print("Falha ao receber o frame da webcam")
                break

          frame_limpo = frame.copy()

          cv2.rectangle(frame, (10, 10), (320, 75), (0, 0, 0), -1)
          cv2.putText(frame, "[ESPAÇO] Salvar foto", (20, 35), fonte, escala, cor_texto, espessura)
          cv2.putText(frame, "[ESPAÇO] Sair", (20, 60), fonte, escala, cor_texto, espessura)
          
          cv2.imshow("Captura de Webcam local", frame)

          tecla = cv2.waitKey(1) & 0xFF
 
          if tecla == 32:
                cv2.imwrite("foto.jpg", frame_limpo)
                print("Foto Salva: foto.jpg")

                foto_cinza = cv2.cvtColor(frame_limpo, cv2.COLOR_BGR2GRAY)
                cv2.imwrite("foto_cinza.jpg", foto_cinza)
                
                foto_invertida = cv2.cvtColor(frame_limpo, cv2.COLOR_RGB2BGR)
                cv2.imwrite("foto_invertida.jpg", foto_invertida)

                foto_roxa = cv2.cvtColor(frame_limpo, cv2.COLOR_RGB2BGR)
                foto_roxa[:, :, 1] = 0
                cv2.imwrite("foto_roxa.jpg", foto_roxa)

          elif tecla == 27:
            print("Encerando câmera...")
            break  
            
    webcam.release()
    cv2.destroyAllWindow()

if __name__ == "__main__":
    capturar_e_salvar()