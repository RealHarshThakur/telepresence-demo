from kubernetes import client, config
from fastapi import FastAPI

app = FastAPI()

config.load_kube_config()




@app.get("/")
async def root():
    pods = [] 
    v1 = client.CoreV1Api()
    print("Listing pods in all namespaces to show that it hot-reloads")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        pods.append(i.metadata.name)

    return {"pods": pods}

