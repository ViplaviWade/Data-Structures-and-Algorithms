# Car Fleet

def car_fleet(target, position, speed):
    stack = []
    cars = sorted(zip(position, speed), reverse=True)
    for p, s in cars:
        time = (target-p)/s
        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)

res = car_fleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])
print(res)