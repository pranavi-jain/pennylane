import numpy as np
import pennylane as qml


## Creating circuit to implement matchgates for XY model using PennyLane

def make_matchgate(params, wire):
    i = wire
    theta_1, theta_2 = params
    qml.RX(np.pi/2, wires=i)
    qml.RX(np.pi/2, wires=i + 1)
    qml.CNOT(wires=[i, i + 1])
    qml.RX(theta_1, wires=i)
    qml.RZ(theta_2, wires=i + 1)
    qml.CNOT(wires=[i, i + 1])
    qml.RX(-np.pi/2, wires=i)
    qml.RX(-np.pi/2, wires=i + 1)
    # matchgate = ProductGate(RZ_layer, RX_layer, cnot, RXRZ_layer, cnot, RX_layer, RZ_layer)
    return


## Create circuit to implement a layer of matchgates on even qubits

def make_layertype1(N, params):
    for i in range(0, N - 1, 2):
        make_matchgate(params, i)
    return


## Create circuit to implement a layer of matchgates on odd qubits

def make_layertype2(N, params):
    # N even
    if N % 2 == 0:
        for i in range(1, N - 1, 2):
            make_matchgate(params, i)
    # N odd
    else:
        for i in range(1, N, 2):
            make_matchgate(params, i)
    return
