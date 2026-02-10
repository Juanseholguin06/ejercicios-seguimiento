class edades:
    @staticmethod
    def calcular_edalber(edjuan):
        return (2 * edjuan) / 3

    @staticmethod
    def calcular_edana(edjuan):
        return (4 * edjuan) / 3
    

    @staticmethod
    def calcular_edmama(edjuan, edalber, edana):
        return (edjuan + edalber + edana)

edjuan = 9

edalber = edades.calcular_edalber(edjuan)
edana = edades.calcular_edana(edjuan)
edmama = edades.calcular_edmama(edalber, edjuan, edana)

print(f"las edades son: alberto = {edalber} ana = {edana} mama = {edmama} juan = {edjuan}")