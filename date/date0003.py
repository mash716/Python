#うるう年の判定
#その年がうるう年かどうかを判定するにはcalendar.isleapを、指定期間内に何回のうるう年があるかを取得するにはcalendar.leapdaysを使用します。

import calendar

print(calendar.isleap(2019))
print(calendar.isleap(2020))
print(calendar.isleap(2021))

print(calendar.leapdays(2020,2021))
