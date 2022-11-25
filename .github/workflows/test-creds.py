import os

from qiskit import IBMQ
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime.accounts import AccountManager

if not IBMQ.stored_account():
    print("No stored account")
    token = os.getenv("PYTKET_REMOTE_QISKIT_TOKEN")
    if token:
        print("Enabling account")
        IBMQ.enable_account(token)
        AccountManager.save(token=token)
else:
    print("Stored account")
    IBMQ.load_account()

provider = IBMQ.get_provider(hub="ibm-q", group="open", project="main")

print("Services:")
print(provider.services())

b = provider.get_backend("ibmq_lima")

print("Made IBMQBackend")

service = QiskitRuntimeService(channel="ibm_quantum")

print("Made QiskitRuntimeService")