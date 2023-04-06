# Задача:
# Задачу о банкомате (из 2-го семинара):
#
# Разбейте её на отдельные операции - функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

log = []
balance = 0
operation_count = 0
flag = True
STEP = 50
COMMISSION_PERCENT = 1.5
MIN_COMMISSION = 30
MAX_COMMISSION = 600
CASH_BACK = 3
WEALTH_THRESHOLD = 5_000_000
TAX_ON_WEALTH = 10

def push_money(amount: int) -> str:
    """
    Функция пополнения счёта с условиями
    :param amount: сумма пополнения
    :return: статус операции, отображение баланса счёта, либо возможной ошибки
    """
    global operation_count, balance, log
    if amount % STEP == 0:
        if amount >= WEALTH_THRESHOLD:
            amount -= amount * TAX_ON_WEALTH / 100
        operation_count += 1
        if operation_count % 3 == 0:
            amount += amount * CASH_BACK / 100
        balance += amount
        log.append(amount)
        result = f'Пополнение успешно выполнено. Баланс: {balance} у.е.'
    else:
        result = f'Сумма внесения должна быть кратна {STEP} у.е.'
    return result


def pull_money(amount: int) -> str:
    """
    Функция снятия средств со счёта с условиями
    :param amount: сумма снятия
    :return: статус операции, отображение баланса счёта, либо возможных ошибок
    """
    global operation_count, balance
    if amount % STEP == 0 and amount <= balance:
        if WEALTH_THRESHOLD <= amount <= (balance - (amount + amount * TAX_ON_WEALTH / 100)):
            balance -= amount * TAX_ON_WEALTH / 100
        elif WEALTH_THRESHOLD <= amount:
            return 'Недостаточно средств на счете для снятия.'

        tax = amount * COMMISSION_PERCENT / 100
        if tax < MIN_COMMISSION:
            tax = MIN_COMMISSION
        elif tax > MAX_COMMISSION:
            tax = MAX_COMMISSION

        if balance - amount - tax >= 0:
            balance = balance - amount - tax
            log.append(-amount)
            operation_count += 1
            if operation_count % 3 == 0:
                balance += amount * CASH_BACK / 100
            result = f'Снятие успешно выполнено. Баланс на счете: {balance} у.е.'
        else:
            result = 'Недостаточно средств на счете для снятия.'
    elif amount % 50 != 0:
        result = f'Сумма снятия должна быть кратна {STEP} у.е.'
    else:
        result = 'Недостаточно средств на счете для снятия.'
    return result


def exit_() -> str:
    """
    Функция завершения работы программы
    :return: отображение текущего баланса счёта, прощание с пользователем
    """
    global flag
    flag = False
    return f'Баланс на счете: {balance} у.е. Работа завершена, до свидания.'


while flag:
    choice = input('Выберите операцию:\n1. Внести средства\n2. Снять средства\n3. История операций\n4. Выход\n')
    if choice == '1':
            replenishment = int(input(f'Введите сумму кратную {STEP} у.е.: '))
            print(push_money(replenishment))
    elif choice == '2':
            withdrawal = int(input(f'Введите сумму кратную {STEP} у.е.: '))
            print(pull_money(withdrawal))
    elif choice == '3':
            for _ in log:
                print(_)
    elif choice == '4':
            print(exit_())
    else:
        print('Ошибка ввода! Выберите из предложенных вариантов')