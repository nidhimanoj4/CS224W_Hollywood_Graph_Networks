#! /usr/bin/python

import snap
import matplotlib.pyplot as plt

G1 = snap.LoadEdgeList(snap.PUNGraph, "edges-100k.txt", 0, 1)

print("G1: Nodes %d, Edges %d" % (G1.GetNodes(), G1.GetEdges()))
print("Number of Nodes: %d" % G1.GetNodes())

# 1.6 number of nodes of zero degree
print("Number of nodes of zero degree: %d" % snap.CntDegNodes(G1, 0))

# Get in degree distribution
DegToCntV = snap.TIntPrV()
snap.GetDegCnt(G1, DegToCntV)
degree = []
numNodes = []
sumDegrees = 0
for item in DegToCntV:
    degree.append(item.GetVal1())
    numNodes.append(item.GetVal2())
    sumDegrees += item.GetVal1()*item.GetVal2()
    #print("%d nodes with in-degree %d" % (item.GetVal2(), item.GetVal1()))

plt.plot(degree, numNodes)
plt.yscale('log')
plt.xscale('log')
plt.ylabel('frequency')
plt.xlabel('degree')
plt.title('Degree distribution')
plt.savefig('degreeDist.png')
plt.clf()

# Get average degree
print("Average degree:", sumDegrees/float(sum(numNodes)))

# Get largest strongly connected component
MxScc = snap.GetMxScc(G1)
print("Size of largest strongly connected component:", MxScc.GetNodes())

# Get strongly connected components
Components = snap.TCnComV()
snap.GetWccs(G1, Components)
wcc_sizes = []
for CnCom in Components:
    wcc_sizes.append(CnCom.Len())

print("Number of connected components:", len(wcc_sizes))

# Clauset-Newman-Moore community detection
CmtyV = snap.TCnComV()
modularity = snap.CommunityCNM(G1, CmtyV)
count = 0
sizes = []
communities = []
for Cmty in CmtyV:
    listcmty = []
    for NI in Cmty:
        listcmty.append(NI)

    communities.append(listcmty)
    count += 1
    sizes.append(len(listcmty))
print("Number of communities:", count)
print("Largest community:", max(sizes))
print("Smallest community:", min(sizes))
print("Community 21:", communities[21])
print("Community 101:", communities[101])
print("Community 10,000:", communities[10000])

# plot histogram of community sizes
sizes.sort()
plt.hist(sizes, log=True)
plt.xlabel("Size of community")
plt.ylabel("Number of communities")
plt.title("Sizes of CNM communities")
plt.show()
plt.savefig("cnm-sizes.png")
#print("Size of communities:", sizes)
print("The modularity of the network is %f" % modularity)
