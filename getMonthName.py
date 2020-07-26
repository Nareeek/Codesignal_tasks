def getMonthName(mo):
    mo -= 1
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if mo >= 0 and mo < len(months):
        return months[mo]
    else:
        return 'invalid month'