def test():
    import os
    g = os.system('systemctl status ufw')
    print(g)

test()
