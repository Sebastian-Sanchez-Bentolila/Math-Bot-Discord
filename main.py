# @Author: Sebastian Sanchez Bentolila - https://github.com/Sebastian-Sanchez-Bentolila

#Modules
import cmath
import math
import matplotlib.pyplot as plt
import random
import os
from decouple import config
from discord import Embed, Color, File
from discord.ext import commands
  
#Main Class       
class Discord():
    def __init__(self):
        self.DISCORD_TOKEN = os.environ.get('TOKEN_DISCORD')
        self.descripcion = 'Bot con diferentes funcionales matemàticas. \n !ayuda'
        self.bot = commands.Bot(command_prefix='!', 
                                description=self.descripcion)
        self.Commands()
    
    
    #Commands   
    def Commands(self):
               
        #Area and Perimeter
        @self.bot.command(name='ap-cuadrado')#Square
        async def AP_Cuadrado(ctx, lado: float):
            area = lado**2
            perimetro = 4 * lado
            embed = Embed(title='Cuadrado', 
                          description='Area = {}\nPerimetro = {}'.format(area, perimetro),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='ap-rectangulo')#Rectangle
        async def AP_Rectangulo(ctx, base: float, altura: float):
            area = base * altura
            perimetro = (2 * base) + (2 * altura)
            embed = Embed(title='Rectangulo', 
                          description='Area = {}\nPerimetro = {}'.format(area, perimetro),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='ap-trapecio')#Trapeze
        async def AP_Trapecio(ctx, base1: float, base2: float, altura: float, a: float, c: float):
            area = ((base1 + base2) * altura)/2
            perimetro = a + base1 + base2 + c
            embed = Embed(title='Trapecio', 
                          description='Area = {}\nPerimetro = {}'.format(area, perimetro),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='ap-paralelogramo')#Parallelogram
        async def AP_Paralelogramo(ctx, base: float, altura: float, a: float):
            area = base * altura
            perimetro = (2 * base) + (2 * a)
            embed = Embed(title='Paralelogramo', 
                          description='Area = {}\nPerimetro = {}'.format(area, perimetro),
                          color=Color.blue())
            await ctx.send(embed=embed)
        
        @self.bot.command(name='ap-rombo')#Rhombus
        async def AP_Rombo(ctx, lado: float, D: float, d: float):
            area = (D * d)/2
            perimetro = 4 * lado
            embed = Embed(title='Rombo', 
                          description='Area = {}\nPerimetro = {}'.format(area, perimetro),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='ap-triangulo-i')#Isosceles Triangle
        async def AP_Triangulo_Isosceles(ctx, base: float, altura: float, a: float):
            area = (base * altura)/2
            perimetro = (2 * a) + base 
            embed = Embed(title='Triangulo Isòsceles', 
                          description='Area = {}\nPerimetro = {}'.format(area, perimetro),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='ap-triangulo-eq')#Equilateral Triangle
        async def AP_Triangulo_Equilatero(ctx, base: float, altura: float, l: float):
            area = (base * altura)/2
            perimetro = 3 * l 
            embed = Embed(title='Triangulo Equilàtero', 
                          description='Area = {}\nPerimetro = {}'.format(area, perimetro),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='ap-triangulo-es')#Scalene Triangle
        async def AP_Triangulo_Escaleno(ctx, base: float, altura: float, a: float, c: float):
            area = (base * altura)/2
            perimetro = base + a + c 
            embed = Embed(title='Triangulo Escaleno', 
                          description='Area = {}\nPerimetro = {}'.format(area, perimetro),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='ap-circulo')#Circle
        async def AP_Circulo(ctx, radio: float):
            area = math.pi * (radio**2)
            perimetro = 2 * math.pi * radio 
            embed = Embed(title='Circulo', 
                          description='Area = {}\nPerimetro = {}'.format(area, perimetro),
                          color=Color.blue())
            await ctx.send(embed=embed)
        
        
        
        
        #Complex Numbers
        @self.bot.command(name='c-resolver')
        async def Complejos(ctx, complejo: str):
            solucion = complex(eval(complejo))
            embed = Embed(title='Numeros Complejos', 
                          description='{} = {}'.format(complejo, solucion),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='c-graficar')
        async def Graficos_Complejos(ctx, titulo: str, complejo: complex):
            real = complejo.real
            imaginario = complejo.imag
            
            
            conjugado = complejo.conjugate()
            modulo = math.sqrt((imaginario**2) + (real**2))
            argumento = (math.atan(imaginario/real) * 180)/math.pi #Convert from radians to degrees
            
            #Cartesian axes graph
            color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
            plt.quiver(0, 0, real, imaginario, angles='xy', scale_units='xy', scale=1, color=color)
            
            if real >= 0 :
                if imaginario >= 0 :
                    plt.axis([0, real, 0, imaginario])
                else:
                    plt.axis([0, real, imaginario, 0])
            else:
                if imaginario >= 0 :
                    plt.axis([real, 0, 0, imaginario])
                else:
                    plt.axis([real, 0, imaginario, 0])
                
            plt.xlabel('Real')
            plt.ylabel('Imaginario')
            plt.title(titulo)
            
            NombreEjes = 'Numeros Complejos (Ejes Cartesianos) '+ str(complejo) + '-Bot de Matemàticas'
            plt.savefig('{}.png'.format(NombreEjes))
            plt.close()
                        
            Ruta_Trabajo = os.getcwd() 
            ImageEjes = ('{}\\{}.png'.format(Ruta_Trabajo, NombreEjes))
            
            #Polar graph
            plt.polar([0, argumento], [0, modulo], marker='o')
            plt.title(titulo)
            
            NombrePolar = 'Numeros Complejos (Gràfico Polar) '+ str(complejo) + '-Bot de Matemàticas'
            plt.savefig('{}.png'.format(NombrePolar))
            plt.close()
            
            ImagePolar = ('{}\\{}.png'.format(Ruta_Trabajo, NombrePolar))
            
            embed = Embed(title='Numeros Complejos', 
                          description='''**{}**
                          
                          Conjugado = {}
                          Modulo = {}
                          Argumento = {}º'''.format(complejo, conjugado, modulo, argumento),
                          color=Color.blue())
            
            await ctx.send(file=File(ImageEjes))
            await ctx.send(embed=embed, file=File(ImagePolar))
            
            
            self.Delete_image()
        
        
        
        #Converter
        @self.bot.command(name='&')
        async def Convertidor(ctx, convertir: str, variable: float):
            #Flat Angle
            #Degrees to Radians
            if convertir == 'grados':
                solucion = (math.pi * variable)/180
                
                embed = Embed(title='Convertidor de Àngulo Plano', 
                              description='{}º = {} rad'.format(variable, solucion),
                              color=Color.blue())
                await ctx.send(embed=embed)
             
            #Radians to Degrees   
            elif convertir == 'radianes':
                solucion = (180 * variable)/math.pi
                
                embed = Embed(title='Convertidor de Àngulo Plano', 
                              description='{} rad = {} º'.format(variable, solucion),
                              color=Color.blue())
                await ctx.send(embed=embed)
            
             
            #Energy   
            #Joule to Calories  
            if convertir == 'julio':
                solucion = variable/4.184
                
                embed = Embed(title='Convertidor de Ènergia', 
                              description='{} J = {} cal'.format(variable, solucion),
                              color=Color.blue())
                await ctx.send(embed=embed)
                
            #Calories to Joule 
            elif convertir == 'cal':
                solucion = variable * 4.184
                
                embed = Embed(title='Convertidor de Ènergia', 
                              description='{} cal = {} J'.format(variable, solucion),
                              color=Color.blue())
                await ctx.send(embed=embed)     
            
            
            #Pressure    
            #Atmosphere to Bar, Pascal and mmHg
            if convertir == 'atsmosfera':
                bar = variable * 1.013
                pascal = variable * 101325
                mmhg = variable * 760
                
                embed = Embed(title='Convertidor de Presiòn', 
                              description='{} atm = {} bar = {} Pa = {} mmHg'.format(variable, bar, pascal, mmhg),
                              color=Color.blue())
                await ctx.send(embed=embed)  
                
            #Bar to Atmosphere, Pascal and mmHg
            elif convertir == 'bar':
                atm = variable/1.013
                pascal = variable * 100000
                mmhg = variable * 750
                
                embed = Embed(title='Convertidor de Presiòn', 
                              description='{} bar = {} atm = {} Pa = {} mmHg'.format(variable, atm, pascal, mmhg),
                              color=Color.blue())
                await ctx.send(embed=embed) 
                
            #Pascal to Atmosphere, Bar and mmHg
            elif convertir == 'pascal':
                atm = variable/101325
                bar = variable/100000
                mmhg = variable/133
                
                embed = Embed(title='Convertidor de Presiòn', 
                              description='{} Pa = {} atm = {} bar = {} mmHg'.format(variable, atm,bar, mmhg),
                              color=Color.blue())
                await ctx.send(embed=embed)
                
            #mmHg to Atmosphere, Bar and Pascal
            elif convertir == 'mmhg':
                atm = variable/760
                bar = variable/750
                pascal = variable * 133
                
                embed = Embed(title='Convertidor de Presiòn', 
                              description='{} mmHg = {} atm = {} bar = {} Pa'.format(variable, atm,bar, pascal),
                              color=Color.blue())
                await ctx.send(embed=embed)
                
            
            #Temperature 
            #Celsius to Fahrenheit and Kelvin  
            if convertir == 'celsius':
                f = ((9/5) * variable) + 32
                k = variable + 273.15
                
                embed = Embed(title='Convertidor de Temperatura', 
                              description='{} ºC = {} ºF = {} K'.format(variable, f, k),
                              color=Color.blue())
                await ctx.send(embed=embed)
                
            #Fahrenheit to Celsius and Kelvin  
            elif convertir == 'fahrenheit':
                c = (variable - 32) * (5/9)
                k = c + 273.15
                
                embed = Embed(title='Convertidor de Temperatura', 
                              description='{} ºF = {} ºC = {} K'.format(variable, c, k),
                              color=Color.blue())
                await ctx.send(embed=embed)
                
            #Kelvin to Celsius and Fahrenheit  
            elif convertir == 'kelvin':
                c = variable - 273.15
                f = ((variable - 273.15) * (9/5)) + 32
                
                embed = Embed(title='Convertidor de Temperatura', 
                              description='{} K = {} ºC = {} ºF'.format(variable, c, f),
                              color=Color.blue())
                await ctx.send(embed=embed)
            
            
            
            
        #Distance between 2 point
        @self.bot.command(name='d-puntos')
        async def Distancia_Puntos(ctx, x1: float, x2: float, y1: float, y2: float):
            distancia = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
            embed = Embed(title='Distancia entre 2 puntos', 
                          description='d = {}'.format(distancia),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        
            
            
        #E constant
        @self.bot.command(name='e')
        async def e(ctx):
            embed = Embed(title='e', 
                          description='{}'.format(math.e),
                          color=Color.blue())
            await ctx.send(embed=embed)
        
        
        
        
        #Functions     
        @self.bot.command(name='f-lineal')#Linear f(x) = m*x + b
        async def Funcion_Lineal(ctx, titulo, *args: str):
            for funciones in args:
                color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
                x = range(-10, 10) 
                
                def f(x):
                    return eval(funciones)
                        
                plt.plot(x, [f(i) for i in x], marker='.', linestyle='-', color=color, label=funciones)
                plt.legend()
                plt.title(titulo)
                
            nombre = 'Funciòn Lineal ' + titulo + '-Bot de Matemàticas'
            plt.savefig('{}.png'.format(nombre))
            plt.close()
                        
            Ruta_Trabajo = os.getcwd() 
            image = ('{}\\{}.png'.format(Ruta_Trabajo, nombre))
                        
            await ctx.send(file=File(image))
                        
            self.Delete_image()
                    
        @self.bot.command(name='f-cuadratica')#Quadratic f(x) = m*(x**2) + b*x + c
        async def Funcion_Cuadratica(ctx, titulo, *args: str):
            for funciones in args:
                color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
                x = range(-10, 10) 
                
                def f(x):
                    return eval(funciones)
                        
                plt.plot(x, [f(i) for i in x], marker='.', linestyle='-', color=color, label=funciones)
                plt.legend()
                plt.title(titulo)
                
            nombre = 'Funciòn Cuadratica ' + titulo + '-Bot de Matemàticas'
            plt.savefig('{}.png'.format(nombre))
            plt.close()
                        
            Ruta_Trabajo = os.getcwd() 
            image = ('{}\\{}.png'.format(Ruta_Trabajo, nombre))
                        
            await ctx.send(file=File(image))
                        
            self.Delete_image()
                    
        @self.bot.command(name='f-cubica')#Cubic f(x) = m*(x**3) + b*(x**2) + c*x + d
        async def Funcion_Cubica(ctx, titulo, *args: str):
            for funciones in args:
                color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
                x = range(-10, 10) 
                
                def f(x):
                    return eval(funciones)
                        
                plt.plot(x, [f(i) for i in x], marker='.', linestyle='-', color=color, label=funciones)
                plt.legend()
                plt.title(titulo)
                
            nombre = 'Funciòn Cùbica ' + titulo + '-Bot de Matemàticas'
            plt.savefig('{}.png'.format(nombre))
            plt.close()
                        
            Ruta_Trabajo = os.getcwd() 
            image = ('{}\\{}.png'.format(Ruta_Trabajo, nombre))
                        
            await ctx.send(file=File(image))
                        
            self.Delete_image()
                    
        @self.bot.command(name='f-exponencial')#Exponential f(x) = a**x
        async def Funcion_Exponencial(ctx, titulo, *args: str):
            for funciones in args:
                color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
                x = range(-10, 10) 
                
                def f(x):
                    return eval(funciones)
                        
                plt.plot(x, [f(i) for i in x], marker='.', linestyle='-', color=color, label=funciones)
                plt.legend()
                plt.title(titulo)
                
            nombre = 'Funciòn Exponencial ' + titulo + '-Bot de Matemàticas'
            plt.savefig('{}.png'.format(nombre))
            plt.close()
                        
            Ruta_Trabajo = os.getcwd() 
            image = ('{}\\{}.png'.format(Ruta_Trabajo, nombre))
                        
            await ctx.send(file=File(image))
                        
            self.Delete_image()
            
        @self.bot.command(name='f-constante')#Constant f(x) = k
        async def Funcion_Constante(ctx, titulo, *args: str):
            for funciones in args:
                color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
                x = range(-10, 10) 
                
                def f(k):
                    return eval(funciones)
                        
                plt.plot(x, [f(i) for i in x], marker='.', linestyle='-', color=color, label=funciones)
                plt.legend()
                plt.title(titulo)
                
            nombre = 'Funciòn Constante ' + titulo + '-Bot de Matemàticas'
            plt.savefig('{}.png'.format(nombre))
            plt.close()
                        
            Ruta_Trabajo = os.getcwd() 
            image = ('{}\\{}.png'.format(Ruta_Trabajo, nombre))
                        
            await ctx.send(file=File(image))
                        
            self.Delete_image()
        
        @self.bot.command(name='f-recta-vertical')#Straight Vertical x = k
        async def Funcion_Recta_Vertical(ctx, titulo, *args: str):
            for funciones in args:
                color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
                y = range(-10, 10) 
                
                def f(k):
                    return eval(funciones)
                        
                plt.plot([f(i) for i in y], y, marker='.', linestyle='-', color=color, label=funciones)
                plt.legend()
                plt.title(titulo)
                
            nombre = 'Funciòn Recta Vertical ' + titulo + '-Bot de Matemàticas'
            plt.savefig('{}.png'.format(nombre))
            plt.close()
                        
            Ruta_Trabajo = os.getcwd() 
            image = ('{}\\{}.png'.format(Ruta_Trabajo, nombre))
                        
            await ctx.send(file=File(image))
                        
            self.Delete_image()  
        
            
            
            
        #General Formula
        @self.bot.command(name='x')
        async def Formula_General(ctx, a: float, b: float, c: float):
            d = (b**2) - (4 * a * c)
            
            if d > 0:
                x1 = ((-b) + (math.sqrt((b**2) - (4 * a * c))) )/(2*a)
                x2 = ((-b) - (math.sqrt((b**2) - (4 * a * c))) )/(2*a)
                embed = Embed(title='Fòrmula General',
                              description='X1 = {}\nX2 = {}'.format(x1, x2),
                              color=Color.blue())
                await ctx.send(embed=embed)
                
            elif d == 0:
                embed = Embed(title='Fòrmula General', 
                              description='Las raìces son reales e iguales',
                              color=Color.blue())
                await ctx.send(embed=embed)
                
            else:
                embed = Embed(title='Fòrmula General', 
                              description='Las raìces no son reales',
                              color=Color.blue())
                await ctx.send(embed=embed)       
        
        
        
        
        #Midpoint between 2 points
        @self.bot.command(name='p-medio')
        async def Punto_medio(ctx, x1: float, x2: float, y1: float, y2: float):
            Xm = (x1 + x2) / 2
            Ym = (y1 + y2) / 2
            embed = Embed(title='Punto medio entre 2 puntos', 
                          description='Xm = {}\nYm = {}'.format(Xm, Ym),
                          color=Color.blue())
            await ctx.send(embed=embed)
         
        
        
            
        #PI constant
        @self.bot.command(name='pi')
        async def pi(ctx):
            embed = Embed(title='PI', 
                          description='{}'.format(math.pi),
                          color=Color.blue())
            await ctx.send(embed=embed)
        
        
        
        
        #Equations
        @self.bot.command(name='r') 
        async def Resolver(ctx, ecuacion):
            resultado = int(eval(ecuacion))
            embed = Embed(title='Ecuaciòn sin incognita', 
                          description='{} = {}'.format(ecuacion, resultado),
                          color=Color.blue())
            await ctx.send(embed=embed)
        
         
         
        #Numbering System
        #Decimal to Binary and Hexadecimal
        @self.bot.command(name='sn-decimal')
        async def Decimal(ctx, decimal: int):
            binario = bin(decimal)
            binario = format(decimal, "b")
            
            hexadecimal = hex(decimal)
            hexadecimal = format(decimal, '0x')
            
            
            embed = Embed(title='Sistema Numèrico', 
                          description=f'{decimal}(10) = {hexadecimal}(16) = {binario}(2)',
                          color=Color.blue())
            await ctx.send(embed=embed)
         
        #Binary to Decimal and Hexadecimal   
        @self.bot.command(name='sn-binario')
        async def Binario(ctx, binario: str):
            decimal = int(binario, base=2)
            
            hexadecimal = hex(decimal)
            hexadecimal = format(decimal, '0x')
            
            embed = Embed(title='Sistema Numèrico', 
                          description=f'{binario}(2) = {decimal}(10) = {hexadecimal}(16)',
                          color=Color.blue())
            await ctx.send(embed=embed)
        
        #Binary to Decimal and Hexadecimal   
        @self.bot.command(name='sn-hexadecimal')
        async def Hexadecimal(ctx, hexadecimal: str):
            hexadecimal.lower()
            
            decimal = int(hexadecimal, base=16)
            
            binario = bin(decimal)
            binario = format(decimal, 'b')
            
            embed = Embed(title='Sistema Numèrico', 
                          description=f'{hexadecimal}(16) = {binario}(2) = {decimal}(10)',
                          color=Color.blue())
            await ctx.send(embed=embed)
            
            
        
                
        #Trignometric functions  
        @self.bot.command(name='t-cos()') #Cos()
        async def Coseno(ctx, x:float):
            coseno = math.cos(x)
            embed = Embed(title='Coseno', 
                          description='cos({}º) = {}'.format(x, coseno),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='t-sin()') #Sin
        async def Seno(ctx, x:float):
            seno = math.sin(x)
            embed = Embed(title='Seno', 
                          description='sen({}º) = {}'.format(x, seno),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='t-tan()') #Tan()
        async def Tangente(ctx, x:float):
            tangente = math.tan(x)
            embed = Embed(title='Tangente', 
                          description='tan({}º) = {}'.format(x, tangente),
                          color=Color.blue())
            await ctx.send(embed=embed)
 
 
 
        #Vector
        @self.bot.command(name='guia')
        async def Guias(ctx, opcion: str):
            
            if opcion == 'numeros-complejos':
                Ruta_Trabajo = os.getcwd()
                ayuda = '{}\\help\\numeros-complejos.txt'.format(Ruta_Trabajo)
            
                embed = Embed(title='Guìas', 
                              color=Color.blue())
                await ctx.send(embed=embed, file=File(ayuda))
                
            if opcion == 'formula-general':
                Ruta_Trabajo = os.getcwd()
                ayuda = '{}\\help\\formula-general.txt'.format(Ruta_Trabajo)
            
                embed = Embed(title='Guìas', 
                              color=Color.blue())
                await ctx.send(embed=embed, file=File(ayuda))
            
            if opcion == 'exponentes':
                Ruta_Trabajo = os.getcwd()
                ayuda = '{}\\help\\propiedades-de-los-exponentes.txt'.format(Ruta_Trabajo)
            
                embed = Embed(title='Guìas', 
                              color=Color.blue())
                await ctx.send(embed=embed, file=File(ayuda))
            
            if opcion == 'radicales':
                Ruta_Trabajo = os.getcwd()
                ayuda = '{}\\help\\npropiedades-de-los-radicales.txt'.format(Ruta_Trabajo)
            
                embed = Embed(title='Guìas', 
                              color=Color.blue())
                await ctx.send(embed=embed, file=File(ayuda))                
            
            
            
            
        #Volume
        @self.bot.command(name='v-cubo') #Cube
        async def Volumen_Cubo(ctx, a: float):
            volumen = a**3
            embed = Embed(title='Cubo', 
                          description='V = {}'.format(volumen),
                          color=Color.blue())
            await ctx.send(embed=embed)  
            
        @self.bot.command(name='v-prisma') #Prism
        async def Volumen_Prisma(ctx, area: float, altura: float):
            volumen = area * altura
            embed = Embed(title='Prisma', 
                          description='V = {}'.format(volumen),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='v-cilindro') #Cylinder
        async def Volumen_Cilindro(ctx, radio: float, altura: float):
            volumen = (math.pi * (radio**2)) * altura
            embed = Embed(title='Cilindro', 
                          description='V = {}'.format(volumen),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='v-esfera') #Sphere
        async def Volumen_Esfera(ctx, radio: float):
            volumen = (4/3) * (math.pi * (radio**3)) 
            embed = Embed(title='Esfera', 
                          description='V = {}'.format(volumen),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='v-piramide') #Pyramid
        async def Volumen_Piramide(ctx, area: float, altura: float):
            volumen = (area*altura)/3 
            embed = Embed(title='Piràmide', 
                          description='V = {}'.format(volumen),
                          color=Color.blue())
            await ctx.send(embed=embed)
            
        @self.bot.command(name='v-cono') #Cone
        async def Volumen_Cono(ctx, radio: float, altura: float):
            volumen = ((math.pi * (radio**2)) * altura)/3 
            embed = Embed(title='Cono', 
                          description='V = {}'.format(volumen),
                          color=Color.blue())
            await ctx.send(embed=embed)




        #About   
        @self.bot.command(name='@') 
        async def About(ctx):
            creator = '@Author: Sebastian Sanchez Bentolila\nhttps://github.com/Sebastian-Sanchez-Bentolila'
            embed = Embed(title='Creator', 
                          description='{}'.format(creator),
                          color=Color.blue())
            await ctx.send(embed=embed)
        
           
            
            
        #Help
        @self.bot.command(name='ayuda')
        async def Ayuda(ctx):
            Ruta_Trabajo = os.getcwd()
            ayuda = '{}\\help\\help.txt'.format(Ruta_Trabajo)
            
            embed = Embed(title='Ayuda bot de Matemàticas', 
                          description='''¡Hola!.
                          ¡Gracias por usar el bot de matemáticas! :)
                          Prefijo = '!' ''',
                          color=Color.blue())
            await ctx.send(embed=embed, file=File(ayuda))
     
     
     
      
    #Bot Run       
    def RunApp(self): 
        self.bot.run(self.DISCORD_TOKEN)
        
    
    
    #Deleting the images in memory
    def Delete_image(self):
        for file in os.listdir():
            if file.endswith('.png'):
                os.remove(file)
        




if __name__ == '__main__':  
    discord = Discord()
    discord.RunApp()