def getAuc(labels, pred):
    pred_sorted = sorted(range(len(pred)), key = lambda i : pred[i])
    pos, neg, auc = 0.0, 0.0, 0.0

    last_pre = pred[pred_sorted[0]]
    count, pre_sum, pos_count = 0.0, 0.0, 0.0

    for i in range(len(pred_sorted)) :
        if labels[pred_sorted[i]] > 0:
            pos += 1
        else:
            neg += 1

        if last_pre != pred[pred_sorted[i]]:
            auc += pos_count * pre_sum / count
            count = 1
            pre_sum = i + 1
            last_pre = pred[pred_sorted[i]]
            if labels[pred_sorted[i]] > 0:
                pos_count = 1
            else:
                pos_count = 0
        else:
            pre_sum += i + 1
            count += 1
            if labels[pred_sorted[i]] > 0:
                pos_count += 1

    auc += pos_count * pre_sum / count
    auc -= pos *(pos + 1) / 2
    auc = auc / (pos * neg)

    return auc


if __name__ == "__main__":

    N = int(input())

    label = [0]*N
    pre = [0]*N

    for i in range(N):
        label[i], pre[i] = map(float, input().split())

    auc=getAuc(label,pre)

    print("%0.2f"%auc)
