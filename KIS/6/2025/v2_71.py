from operator import xor


def main(keta):
    negro = {2 * k - k % 3 for k in keta if k > -9}
    omega = {2 * v - v ** 3 for v in negro if xor(v >= -55, v < 18)}
    egor = {k - 5 * v for k in keta for v in negro if k > v}
    beta = {e % 3 + e ** 2 for e in egor if e <= -15}

    return len(omega) - sum(b for b in beta)
