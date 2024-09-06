import json

from fastapi import FastAPI
from kafka import KafkaProducer
from pydantic import BaseModel

app = FastAPI()
producer = KafkaProducer(
    bootstrap_servers="kafka:9092", value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


@app.get("/visit")
async def visit():
    # Create a visit event
    visit_event = {"event": "visit"}

    # Send event to Kafka
    producer.send("visits", visit_event)
    producer.flush()

    return {"message": "Visit recorded"}
