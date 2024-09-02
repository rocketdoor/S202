from database import Database
from writeAJson import writeAJson
import threading as th
import time
import random

def checaTemp1(database, intervalo):
    local1 = {"nomeSensor": "Temp1"}
    temp1 = database.collection.find(local1)
    while database.collection.find_one({"nomeSensor": "Temp1", "sensorAlarmado": False}):
        novoValor = {"$set": {"valorSensor": round(random.uniform(30,40), 2)}}
        database.collection.update_one(local1, novoValor)
        writeAJson(temp1, "Temperatura1")
        time.sleep(intervalo)
        if database.collection.find_one({"nomeSensor": "Temp1", "valorSensor":{"$gt":38}}):
           print("\nAtencao! Temperatura muito alta! Verificar Sensor 1")
           novoValor = {"$set": {"sensorAlarmado": True}}
           database.collection.update_one(local1, novoValor)
           break
    writeAJson(temp1, "Temperatura1")

def checaTemp2(database, intervalo):
    local2 = {"nomeSensor": "Temp2"}
    temp2 = database.collection.find(local2)
    while database.collection.find_one({"nomeSensor": "Temp2", "sensorAlarmado": False}):
        novoValor = {"$set": {"valorSensor": round(random.uniform(30,40), 2)}}
        database.collection.update_one(local2, novoValor)
        writeAJson(temp2, "Temperatura2")
        time.sleep(intervalo)
        if database.collection.find_one({"nomeSensor": "Temp2", "valorSensor":{"$gt":38}}):
           print("\nAtencao! Temperatura muito alta! Verificar Sensor 2")
           novoValor = {"$set": {"sensorAlarmado": True}}
           database.collection.update_one(local2, novoValor)
           break
    writeAJson(temp2, "Temperatura2")

def checaTemp3(database, intervalo):
    local3 = {"nomeSensor": "Temp3"}
    temp3 = database.collection.find(local3)
    while database.collection.find_one({"nomeSensor": "Temp3", "sensorAlarmado": False}):
        novoValor = {"$set": {"valorSensor": round(random.uniform(30,40), 2)}}
        database.collection.update_one(local3, novoValor)
        writeAJson(temp3, "Temperatura3")
        time.sleep(intervalo)
        if database.collection.find_one({"nomeSensor": "Temp3", "valorSensor":{"$gt":38}}):
           print("\nAtencao! Temperatura muito alta! Verificar Sensor 3")
           novoValor = {"$set": {"sensorAlarmado": True}}
           database.collection.update_one(local3, novoValor)
           break
    writeAJson(temp3, "Temperatura3")


db = Database(database="bancoiot", collection="sensores")
#db.resetDatabase()

valorPadrao = {"$set": {"valorSensor": 0}}
configuracaoPadrao = {"$set": {"sensorAlarmado": False}}

local1 = {"nomeSensor": "Temp1"}
db.collection.update_one(local1, valorPadrao)
db.collection.update_one(local1, configuracaoPadrao)

local2 = {"nomeSensor": "Temp2"}
db.collection.update_one(local2, valorPadrao)
db.collection.update_one(local2, configuracaoPadrao)

local3 = {"nomeSensor": "Temp3"}
db.collection.update_one(local3, valorPadrao)
db.collection.update_one(local3, configuracaoPadrao)

intervalo = 5

temp1 = th.Thread(target = checaTemp1, args=(db, intervalo))
temp2 = th.Thread(target = checaTemp2, args=(db, intervalo))
temp3 = th.Thread(target = checaTemp3, args=(db, intervalo))
temp1.start()
temp2.start()
temp3.start()

