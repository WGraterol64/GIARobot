import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Grua(object):
	
	def __init__(self, pinY, pinW, pinB, pinR):
		"""Inicializacion de una instancia de la clase Grua.
		
		Parametros:
		pinY: Pin del Puente H perteneciente a la pareja Amarillo-Blanco (Actual 24).
		pinW: Pin del Puente H perteneciente a la pareja Amarillo-Blanco (Actual 23).
		pinB: Pin del Puente H perteneciente a la pareja Azul-Rojo (Actual 22).
		pinR: Pin del Puente H perteneciente a la pareja Azul-Rojo (Actual 27). """
		
		self.pinY = pinY
		self.pinW = pinW
		self.pinB = pinB
		self.pinR = pinR


		# Set pin states
		GPIO.setup(pinY, GPIO.OUT)
		GPIO.setup(pinW, GPIO.OUT)
		GPIO.setup(pinB, GPIO.OUT)
		GPIO.setup(pinR, GPIO.OUT)

	
	def setStep(w1, w2, w3, w4):
		"""Prende o apaga los pines del Puente H, 1 para prendido y 0 para apagado.
		
		Parametros:
		w1: Pin del Puente H de la pareja Amarillo-Blanco.
		w2: Pin del Puente H de la pareja Amarillo-Blanco.
		w3: Pin del Puente H de la pareja Azul-Rojo.
		w4: Pin del Puente H de la pareja Azul-Rojo. """
		
		GPIO.output(pinY, w1)
		GPIO.output(pinW, w2)
		GPIO.output(pinB, w3)
		GPIO.output(pinR, w4)


	def stepper(steps, delay):
		"""Hace girar el Stepper Motor "steps" pasos con un retraso de "delay" segundos entre cada paso. 
			
			Parametros:
			steps: Numero de pasos que girara el Stepper Motor. El sentido del giro esta determinado por 
				el signo de este parametro.
			delay: Tiempo de espera entre cada paso. Mientras mas alto el valor, mas tarda en girar el Stepper 
				Motor. Se recomienda un valor de 0.0055."""
			
		if steps > 0:
			for i in range(0, steps):
				setStep(1,0,1,0)
				time.sleep(delay)
				setStep(0,1,1,0)
				time.sleep(delay)
				setStep(0,1,0,1)
				time.sleep(delay)
				setStep(1,0,0,1)
				time.sleep(delay)
				
		else:
			for i in range(0, -steps):
				setStep(1,0,0,1)
				time.sleep(delay)
				setStep(0,1,0,1)
				time.sleep(delay)
				setStep(0,1,1,0)
				time.sleep(delay)
				setStep(1,0,1,0)
				time.sleep(delay)

