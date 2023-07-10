# 平滑的加权轮询算法
initWeight = {'node-1': 9, 'node-2': 6, 'node-3': 8, 'node-4': 10}
currentWeight = {'node-1': 0, 'node-2': 0, 'node-3': 0, 'node-4': 0}
hitNode = {}    # 节点命中情况
hitNodeCnt = {}     # 节点命中次数
initWeightSum = sum(initWeight.values())


def calculate():
    for i in range(1, 41):
        # 计算当前权重
        for j in range(1, 5):
            node = 'node-' + str(j)
            currentWeight[node] += initWeight[node]

        # 选出节点
        max_value = max(currentWeight.values())
        max_keys = [key for key, value in currentWeight.items() if value == max_value]
        hit = max_keys[0]   # 无论多少个 key，只选第一个（随机）
        hitNode[i] = hit
        hitNodeCnt[hit] = hitNodeCnt.get(hit, 0) + 1

        # 扣减当前权重
        currentWeight[hit] -= initWeightSum


if __name__ == '__main__':
    calculate()

    for k, v in hitNode.items():
        print('轮次:', k, '，命中节点:', v)

    print('============================')

    for k, v in hitNodeCnt.items():
        print('节点:', k, '，命中次数:', v)
