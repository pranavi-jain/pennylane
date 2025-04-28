import pennylane as qml


## Creating circuit to implement matchgates using PennyLane

def make_matchgate(params, wire):
    i = wire
    qml.RZ(params[0], wires=i)
    qml.RZ(params[1], wires=i + 1)
    qml.RX(params[2], wires=i)
    qml.RX(params[3], wires=i + 1)
    qml.CNOT(wires=[i, i + 1])
    qml.RX(params[4], wires=i)
    qml.RZ(params[5], wires=i + 1)
    qml.CNOT(wires=[i, i + 1])
    qml.RX(params[6], wires=i)
    qml.RX(params[7], wires=i + 1)
    qml.RZ(params[8], wires=i)
    qml.RZ(params[9], wires=i + 1)
    # matchgate = (RZ_layer * RX_layer * cnot * RXRZ_layer * cnot * RX_layer * RZ_layer)


def make_layertype1(N, params):
    for i in range(0, N - 1, 2):
        make_matchgate(params, i)
    qml.Barrier(wires=range(N))
    return


def make_layertype2(N, params):
    # N even
    if N % 2 == 0:
        for i in range(1, N - 1, 2):
            make_matchgate(params, i)
    # N odd
    else:
        for i in range(1, N, 2):
            make_matchgate(params, i)
    qml.Barrier(wires=range(N))
    return
