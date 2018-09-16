import vk_api
import datetime
import time

while True:
    vk = vk_api.VkApi(token="6f09477ca6e1b7e060b92835ae0ee2c0704bffa30a318d6e8aaa67b9c21009b2708aeb5e773c18d09fdd7")

    delta = datetime.timedelta(hours=3, minutes=0)
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)
    nowtime = t.strftime("%H:%M")
    nowdate = t.strftime("%d.%m.%Y")

    on = vk.method("friends.getOnline")
    counted = len(on)

    vk.method("status.set", {"text": nowtime + " ● " + nowdate + " ● " + "Друзей онлайн: " + str(counted)})

    time.sleep(30)
