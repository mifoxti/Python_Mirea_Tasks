def main(f):
    os = {abs(fm) for fm in f if fm >= -75 and fm <= 24}
    k = {6 * fm - abs(fm) for fm in f if fm <= 82 and fm >= -43}
    o = {abs(km) + 6 * w for km in k for w in os if km > w}
    e = len(os) - sum(abs(om) for om in o)
    return e
