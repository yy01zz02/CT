        elif isinstance(self.igra, Pop10_logika):
            # Imamo Pop 10 igro
            if self.igra.faza == 1:
                # Smo v fazi odstranjevanja žetonov
                zeljen_vrstni_red = random.sample([18, 68, 25, 75], 4) # Središčni dve polji
                dodajamo = [10, 11, 12, 17, 19, 24, 26, 31, 32, 33]
                dodajamo += [50+i for i in dodajamo]
                zeljen_vrstni_red += random.sample(dodajamo, len(dodajamo))
                dodajamo = [i for i in range(2, 7)] + [i for i in range(37, 42)] + [9+7*i for i in range(4)] + [13+7*i for i in range(4)]
                dodajamo += [50+i for i in dodajamo]
                zeljen_vrstni_red += random.sample(dodajamo, len(dodajamo))
                dodajamo = [1+7*i for i in range(6)] + [7+7*i for i in range(6)]
                dodajamo += [50+i for i in dodajamo]
                zeljen_vrstni_red += random.sample(dodajamo, len(dodajamo))                
            else:
                # Smo v fazi dodajanja žetonov (lahko faza 0 ali 2)
                zeljen_vrstni_red = [4]
                for i in range(1,4):
                    zeljen_vrstni_red += random.sample([4+i, 4-i], 2)
        else: