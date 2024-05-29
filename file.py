#Script

vocals = ["a","e","i","o","u"]

subject = input('Ingresa tu nombre: ')

num_vocals = 0

for item in list(subject):
 if item in vocals:
    num_vocals += 1

if num_vocals >=3:
    print(f'Tu nombre es: {subject} y tiene tres o mas vocales')
          
else:

    print("Tu nombre no tiene tres vocales!")
