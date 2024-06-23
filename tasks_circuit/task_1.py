import numpy as np

def calculate_resistances_and_currents(U, R1, R2, R3, R4):
    # Шаг 1: Определение эквивалентного сопротивления R34
    R34 = R3 + R4

    # Шаг 2: Определение эквивалентного сопротивления для параллельного соединения R1 и R34
    R134 = (R34 * R1) / (R34 + R1)

    # Шаг 3: Определение эквивалентного сопротивления Rэкв для последовательного соединения R134 и R2
    R_ekv = R134 + R2

    # Шаг 4: Определение тока I
    I = U / R_ekv

    # Шаг 5: Определение токов в параллельных ветвях
    if R34 != R1:
        I2 = I * R34 / (R34 + R1)  # Ток через R1
        I1 = I - I2  # Ток через R34
    else:
        I1 = I2 = I / 2

    # Шаг 6: Определение напряжений
    V1 = U
    V2 = V1 - I2 * R1
    V3 = V2 + I1 * R4

    return V1, V2, V3, I, I1, I2


def main():
    R1 = float(input("Введите значение R1 (в Омах): "))
    R2 = float(input("Введите значение R2 (в Омах): "))
    R3 = float(input("Введите значение R3 (в Омах): "))
    R4 = float(input("Введите значение R4 (в Омах): "))
    Vbias = float(input("Введите значение Vbias (в Вольтах): "))

    V1, V2, V3, I, I1, I2 = calculate_resistances_and_currents(Vbias, R1, R2, R3, R4)

    print(f"Напряжение в узле 1 (V1): {V1:.3f} В")
    print(f"Напряжение в узле 2 (V2): {V2:.3f} В")
    print(f"Напряжение в узле 3 (V3): {V3:.3f} В")
    print(f"Ток через источник напряжения (I): {I:.3f} А")
    print(f"Ток I1 = {I1:.3f} А (ток через R4)")
    print(f"Ток I2 = {I2:.3f} А (ток через R1)")


if __name__ == "__main__":
    main()