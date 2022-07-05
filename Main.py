
'''
Created on 5 jul 2022

@author: osvaldo.hernandez
'''
fichero=open("Clientes.txt", "r")
lista=fichero.readlines()
import requests

x=[]
aux1=0
while aux1<len(lista):
    txt=lista[aux1]
    x=txt.split(", ")
    #print(x)
    employee={'suername': x[0], 'firstname': x[1]}
    print(employee)
    resp = requests.post("http://localhost:8080/apiv1/employee/add", json=employee).json()
    #print(resp)
    country={"code": x[2], "name": x[3]}
    print(country)
    resp = requests.post("http://localhost:8080/apiv1/country/add", json=country).json()
    lenguage={"codee": x[4], "namee": x[5]}
    print(lenguage)
    resp = requests.post("http://localhost:8080/apiv1/lenguage/add", json=lenguage).json()
    air={"name": x[6]}
    print(air)
    resp = requests.post("http://localhost:8080/apiv1/air/add", json=air).json()
    aux1 +=1 

