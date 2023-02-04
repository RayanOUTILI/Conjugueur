def conjugaison():
    verbe=input("Bonjour,quel verbe souhaitez-vous conjuguer ? ")
    print(" ")
    infinitif=verbe[-2:]
    radical=verbe[0:-2]
    voyelle=["a","e","i","o","u","y"]
    exceptioncmer=["offrir","ouvrir","souffrir","cueillir"]
    verbeendre=verbe[0:-1]
    réponsetemps=input("A quel temps souhaitez-vous conjuguer le verbe"+" "+verbe+" "+"?Vous avez le choix entre le passé composé,passé simple,l'imparfait le présent ou le futur. ")
    print(" ")
    if réponsetemps=="présent":
        réponsemode=input("A quel mode souhaitez-vous conjuguer ce verbe ? Vous avez le choix entre le présent : indicatif, conditionnel,impératif, subjonctif ou gérondif.")
        print("")
        if réponsemode=="indicatif":
            print("Voici le verbe"+" "+verbe+" "+"au présent de l'indicatif, à toutes les personnes")
            print("")
            if verbe=="aller":
                print("Je"+" "+"vais")
                print("Tu"+" "+"vas")
                print("Il/Elle/On"+" "+"va")
                print("Nous"+" "+"allons")
                print("Vous"+" "+"allez")
                print("Ils/Elles"+" "+"vont")

            elif verbe=="être":
                print("Je"+" "+"suis")
                print("Tu"+" "+"es")
                print("Il/Elle/On"+" "+"est")
                print("Nous"+" "+"sommes")
                print("Vous"+" "+"êtes")
                print("Ils/Elles"+" "+"sont")

            elif verbe=="avoir":
                print("J'ai")
                print("Tu"+" "+"as")
                print("Il/Elle/On"+" "+"a")
                print("Nous"+" "+"avons")
                print("Vous"+" "+"avez")
                print("Ils/Elles"+" "+"ont")

            elif verbe=="voir":
                print("Je vois")
                print("Tu vois")
                print("Il/Elle/On voit")
                print("Nous voyons")
                print("Vous voyez")
                print("Ils/Elles voient")

            elif verbe=="prendre":
                print("Je"+" "+radical+"s")
                print("Tu"+" "+radical+"s")
                print("Il/Elle/On"+" "+radical)
                print("Nous"+" "+"prennons")
                print("Vous"+" "+"prennez")
                print("Ils/Elles"+" "+"prennent")

            elif verbe=="pouvoir":
                print("Je"+" "+"peux")
                print("Tu"+" "+"peux")
                print("Il/Elle/On"+" "+"peut")
                print("Nous"+" "+"pouvons")
                print("Vous"+" "+"pouvez")
                print("Ils/Elles"+" "+"peuvent")

            elif verbe=="vouloir":
                print("Je"+" "+"veux")
                print("Tu"+" "+"veux")
                print("Il/Elle/On"+" "+"veut")
                print("Nous"+" "+"voulons")
                print("Vous"+" "+"voulez")
                print("Ils/Elles"+" "+"veulent")

            elif verbe=="coudre":
                print("Je"+" "+radical+"s")
                print("Tu"+" "+radical+"s")
                print("Il/Elle/On"+" "+radical)
                print("Nous"+" "+"cousons")
                print("Vous"+" "+"cousez")
                print("Ils/Elles"+" "+"cousent")

            elif verbe[-3:]=="tre":#ex mettre
                print("Je"+" "+radical[:-1]+"s")
                print("Tu"+" "+radical[:-1]+"s")
                print("Il/Elle/On"+" "+radical[:-1])
                print("Nous"+" "+radical+"ons")
                print("Vous"+" "+radical+"ez")
                print("Ils/Elles"+" "+radical+"ent")

            elif verbe[-6:]=="cevoir":#apercevoir concevoir
                if verbe[0:1] in voyelle:
                    print("J'"+radical[:-4]+"çois")
                else:
                    print("Je"+" "+radical[:-4]+"çois")
                print("Tu"+" "+radical[:-4]+"çois")
                print("Il/Elle/On"+" "+radical[:-4]+"çoit")
                print("Nous"+" "+radical[:-4]+"cevons")
                print("Vous"+" "+radical[:-4]+"cevez")
                print("Ils/Elles"+" "+radical[:-4]+"çoivent")

            elif verbe[-3:]=="ger":# ex manger nager
                if verbe[0:1] in voyelle:
                    print("J'"+radical+"e")
                else:
                    print("Je"+" "+radical+"e")
                print("Tu"+" "+radical+"es")
                print("Il/Elle/On"+" "+radical+"e")
                print("Nous"+" "+radical+"eons")
                print("Vous"+" "+radical+"ez")
                print("Ils/Elles"+" "+radical+"ent")

            elif verbe[-3:]=="cer":# ex lancer annoncer
                if verbe[0:1] in voyelle:
                    print("J'"+radical+"e")
                else:
                    print("Je"+" "+radical+"e")
                print("Tu"+" "+radical+"es")
                print("Il/Elle/On"+" "+radical+"e")
                print("Nous"+" "+radical[:-1]+"çons")
                print("Vous"+" "+radical+"ez")
                print("Ils/Elles"+" "+radical+"ent")

            elif verbe[-2:]=="er":
            #au cas où la première lettre du verbe est une voyelle ex: j'arrive et non pas je arrive
                if verbe[0:1] in voyelle:
                    print("J'"+radical+"e")
                else:
                    print("Je"+" "+radical+"e")
                print("Tu"+" "+radical+"es")
                print("Il/Elle/On"+" "+radical+"e")
                print("Nous"+" "+radical+"ons")
                print("Vous"+" "+radical+"ez")
                print("Ils/Elles"+" "+radical+"ent")

            elif verbe in exceptioncmer:
                if verbe[0:1] in voyelle:
                    print("J'"+radical+"e")
                else:
                    print("Je"+" "+radical+"e")
                print("Tu"+" "+radical+"es")
                print("Il/Elle/On"+" "+radical+"e")
                print("Nous"+" "+radical+"ons")
                print("Vous"+" "+radical+"ez")
                print("Ils/Elles"+" "+radical+"ent")

            elif verbe[-3:]=="dre": #ex vendre
                if verbe[0:1] in voyelle:
                    print("J'"+radical+"s")
                else:
                    print("Je"+" "+radical+"s")
                print("Tu"+" "+radical+"s")
                print("Il/Elle/On"+" "+radical)
                print("Nous"+" "+radical+"ons")
                print("Vous"+" "+radical+"ez")
                print("Ils/Elles"+" "+radical+"ent")
            
            elif verbe[-4:]=="enir":#venir obtenir..
                if verbe[0:1] in voyelle:
                    print("J'"+radical[:-2]+"iens")
                else:
                    print("Je"+" "+radical[:-2]+"iens")
                print("Tu"+" "+radical[:-2]+"iens")
                print("Il/Elle/On"+" "+radical[:-2]+"ient")
                print("Nous"+" "+radical[:-2]+"enons")
                print("Vous"+" "+radical[:-2]+"enez")
                print("Ils/Elles"+" "+radical[:-2]+"iennent")
                    
            elif verbe[-2:]=="ir":
                if verbe[0:1] in voyelle:
                    print("J'"+radical+"is")
                else:
                    print("Je"+" "+radical+"is")
                print("Tu"+" "+radical+"is")
                print("Il/Elle/On"+" "+radical+"it")
                print("Nous"+" "+radical+"issons")
                print("Vous"+" "+radical+"issez")
                print("Ils/Elles"+" "+radical+"issent")

            else:
                if verbe[0:1] in voyelle:
                    print("J'"+radical+"s")
                else:
                    print("Je"+" "+radical+"s")
                print("Tu"+" "+radical+"s")
                print("Il/Elle/On"+" "+radical+"t")
                print("Nous"+" "+radical+"ons")
                print("Vous"+" "+radical+"ez")
                print("Ils/Elles"+" "+radical+"ent")

        elif réponsemode=="gérondif":
            print("Voici le verbe"+" "+verbe+" "+"au gérondif présent:")
            print(" ")
            if verbe=="apprendre":
                print("en"+" "+radical[:-1]+"ant")

            elif verbe=="faire":
                print("en faisant")

            elif verbe=="boire":
                print("en buvant")

            elif verbe=="connaître":
                print("en connaissant")

            elif verbe=="croire":
                print("en croyant")

            elif verbe=="voir":
                print("en voyant")

            elif verbe=="avoir":
                print("en ayant")

            elif verbe=="être":
                print("en étant")

            elif verbe=="savoir":
                print("en sachant")

            elif verbe=="peindre":
                print("en peignant")

            elif verbe=="faire":
                print("en faisant")

            elif verbe[-3:]=="ger":
                print("en"+" "+radical+"eant")

            elif verbe[-3:]=="cer":
                print("en"+" "+radical[:-1]+"çant")

            else:
                vbpronominaux=verbe[2:-2]
                if verbe[0:2]=="se":#ex se doucher
                    print("en"+" "+"se"+vbpronominaux+"ant")

                elif verbe[0:2]=="s'":#ex s'appeler
                    print("en"+" "+"se"+vbpronominaux+"ant")
                else:
                    print("en"+" "+radical+"ant")

        elif réponsemode=="conditionnel":
            print("Voici le verbe"+" "+verbe+" "+"au gérondif présent:")
            print(" ")
            if verbe=="avoir":
                print("J'aurais")
                print("Tu aurais")
                print("Il/Elle/On aurait")
                print("Nous aurions")
                print("Vous auriez")
                print("Ils/Elles auraient")

            elif verbe=="être":
                print("Je serais")
                print("Tu serais")
                print("Il/Elle/On serait")
                print("Nous serions")
                print("Vous seriez")
                print("Ils/Elles seraient")

            else:
                if verbe[0:1] in voyelle:
                    print("J'"+verbe+"ais")
                else:
                    print("Je"+" "+verbe+"ais")
                print("Tu"+" "+verbe+"ais")
                print("Il/Elle/On"+" "+verbe+"ait")
                print("Nous"+" "+verbe+"ions")
                print("Vous"+" "+verbe+"iez")
                print("Ils/Elles"+" "+verbe+"aient")
        
        elif réponsemode=="subjonctif":
            print("Voici le verbe"+" "+verbe+" "+"au subjonctif présent:")
            print(" ")
            if verbe=="avoir":
                print("J'aie")
                print("Tu aies")
                print("Il/Elle/On ait")
                print("Nous ayons")
                print("Vous ayez")
                print("Ils/Elles aient")
            
            elif verbe=="être":
                print("Je sois")
                print("Tu sois")
                print("Il/Elle/On soit")
                print("Nous soyons")
                print("Vous soyez")
                print("Ils/Elles soient")
            
            elif verbe=="faire":
                print("Je fasse")
                print("Tu fasses")
                print("Il/Elle/On fasse")
                print("Nous fassions")
                print("Vous fassiez")
                print("Ils/Elles fassent")
            
            elif verbe=="aller":
                print("J'aille")
                print("Tu ailles")
                print("Il/Elle/On aille")
                print("Nous allions")
                print("Vous alliez")
                print("Ils/Elles aillent")
            
            elif verbe[-4:]=="enir":#ex venir tenir
                if verbe[0:1] in voyelle:
                    print("J'"+radical[:-2]+"ienne")
                else:
                    print("Je"+" "+radical[:-2]+"ienne")
                print("Tu"+" "+radical[:-2]+"iennes")
                print("Il/Elle/On"+" "+radical[:-2]+"ienne")
                print("Nous"+" "+radical[:-2]+"enions")
                print("Vous"+" "+radical[:-2]+"eniez")
                print("Ils/Elles"+" "+radical[:-2]+"iennent")
            
            elif verbe=="er":
                if verbe[0:1] in voyelle:
                    print("J'"+radical+"e")
                else:
                    print("Je"+" "+radical+"e")
                print("Tu"+" "+radical+"es")
                print("Il/Elle/On"+" "+radical+"e")
                print("Nous"+" "+radical+"ions")
                print("Vous"+" "+radical+"iez")
                print("Ils/Elles"+" "+radical+"ent")
            
            elif verbe=="ir":
                if verbe[0:1] in voyelle:
                    print("J'"+radical+"isse")
                else:
                    print("Je"+" "+radical+"isse")
                print("Tu"+" "+radical+"isses")
                print("Il/Elle/On"+" "+radical+"isse")
                print("Nous"+" "+radical+"issions")
                print("Vous"+" "+radical+"issiez")
                print("Ils/Elles"+" "+radical+"issent")
            
            else:
                if verbe[0:1] in voyelle:
                    print("J'"+radical+"e")
                else:
                    print("Je"+" "+radical+"e")
                print("Tu"+" "+radical+"es")
                print("Il/Elle/On"+" "+radical+"e")
                print("Nous"+" "+radical+"ions")
                print("Vous"+" "+radical+"iez")
                print("Ils/Elles"+" "+radical+"ent")
        
        elif réponsemode=="impératif":
            print("Voici le verbe"+" "+verbe+" "+"à l'impératif présent:")
            print(" ")
            if verbe=="être":
                print("sois")
                print("soyons")
                print("soyez")
            
            elif verbe=="avoir":
                print("aie")
                print("ayons")
                print("ayez")
            
            elif verbe=="savoir":
                print("sache")
                print("sachons")
                print("sachez")
            
            elif verbe=="sortir":
                print("sors")
                print("sortons")
                print("sortez")
                
            elif verbe[-2:]==er:
                print(radical+"e")
                print(radical+"ons")
                print(radical+"ez")
            
            elif verbe[-2:]=="ir":
                print(radical+"is")
                print(radical+"issons")
                print(radical+"issez")
            
            else:
                print(radical+"s")
                print(radical+"ons")
                print(radical+"ez")
                
        else:
            print("Réessayez avec gérondif,indicatif, subjonctif, impératif ou conditionnel !")

    elif réponsetemps=="imparfait":
            print("Voici le verbe"+" "+verbe+" "+"à l'imparfait:")
            print(" ")
            if verbe=="être":
                print("J'étais")
                print("Tu étais")
                print("Il/Elle/On était")
                print("Nous étions")
                print("Vous étiez")
                print("Ils/Elles étaient")

            elif verbe=="avoir":
                print("J'avais")
                print("Tu avais")
                print("Il/Elle/On avait")
                print("Nous avions")
                print("Vous aviez")
                print("Ils/Elles avaient")

            elif verbe=="faire":
                print("Je faisais")
                print("Tu faisais")
                print("Il/Elle/On faisait")
                print("Nous faisions")
                print("Vousfaisiez")
                print("Ils/Elles faisaient")

            elif verbe[-5:]=="endre":#prendre apprendre..
                if verbe[0:1] in voyelle:
                    print("J'"+radical[:-1]+"ais")
                else:
                    print("Je"+" "+radical[:-1]+"ais")
                print("Tu"+" "+radical[:-1]+"ais")
                print("Il/Elle/On"+" "+radical[:-1]+"ait")
                print("Nous"+" "+radical[:-1]+"ions")
                print("Vous"+" "+radical[:-1]+"iez")
                print("Ils/Elles"+" "+radical[:-1]+"aient")

            elif verbe[-3:]=="ger":
                if verbe[0:1] in voyelle:
                    print("J'"+radical+"eais")
                else:
                    print("Je"+" "+radical+"eais")
                print("Tu"+" "+radical+"eais")
                print("Il/Elle/On"+" "+radical+"eait")
                print("Nous"+" "+radical+"ions")
                print("Vous"+" "+radical+"iez")
                print("Ils/Elles"+" "+radical+"eaient")

            elif verbe[-3:]=="cer":#ex placer
                if verbe[0:1] in voyelle:
                    print("J'"+radical[:-1]+"çais")
                else:
                    print("Je"+" "+radical[:-1]+"çais")
                print("Tu"+" "+radical[:-1]+"çais")
                print("Il/Elle/On"+" "+radical[:-1]+"çait")
                print("Nous"+" "+radical[:-1]+"cions")
                print("Vous"+" "+radical[:-1]+"ciez")
                print("Ils/Elles"+" "+radical[:-1]+"çaient")

            elif verbe[-3:]=="oir":#vouloir
                if verbe[0:1] in voyelle:
                    print("J'"+radical[:-1]+"ais")
                else:
                    print("Je"+" "+radical[:-1]+"ais")
                print("Tu"+" "+radical[:-1]+"ais")
                print("Il/Elle/On"+" "+radical[:-1]+"ait")
                print("Nous"+" "+radical[:-1]+"ions")
                print("Vous"+" "+radical[:-1]+"iez")
                print("Ils/Elles"+" "+radical[:-1]+"aient")

            else:
                if verbe[0:1] in voyelle:
                    print("J'"+radical+"ais")
                else:
                    print("Je"+" "+radical+"ais")
                print("Tu"+" "+radical+"ais")
                print("Il/Elle/On"+" "+radical+"ait")
                print("Nous"+" "+radical+"ions")
                print("Vous"+" "+radical+"iez")
                print("Ils/Elles"+" "+radical+"aient")

    elif réponsetemps=="futur":
        print(" ")
        if verbe=="aller":
            print("Voici le verbe"+" "+verbe+" "+"au futur, à toutes les personnes")
            print("J'"+" "+"irai")
            print("Tu"+" "+"iras")
            print("Il/Elle/On"+" "+"ira")
            print("Nous"+" "+"irons")
            print("Vous"+" "+"irez")
            print("Ils/Elles"+" "+"iront")

        elif verbe=="faire":
            print("Voici le verbe"+" "+verbe+" "+"au futur, à toutes les personnes")
            faireauftr=["ferai","feras","fera","ferons","ferez","ferons"]
            print("Je"+" "+faireauftr[0])
            print("Tu"+" "+faireauftr[1])
            print("Il/Elle/On"+" "+faireauftr[2])
            print("Nous"+" "+faireauftr[3])
            print("Vous"+" "+faireauftr[4])
            print("Ils/Elles"+" "+faireauftr[5])

        elif verbe=="venir":
            print("Voici le verbe"+" "+verbe+" "+"au futur, à toutes les personnes")
            venirauftr=["viendrai","viendras","viendra","viendrons","viendrez","viendront"]
            print("Je"+" "+venirauftr[0])
            print("Tu"+" "+venirauftr[1])
            print("Il/Elle/On"+" "+venirauftr[2])
            print("Nous"+" "+venirauftr[3])
            print("Vous"+" "+venirauftr[4])
            print("Ils/Elles"+" "+venirauftr[5])

        elif verbe=="tenir":
            print("Voici le verbe"+" "+verbe+" "+"au futur, à toutes les personnes")
            tenirauftr=["tiendrai","tiendras","tiendra","tiendrons","tiendrez","tiendront"]
            print("Je"+" "+tenirauftr[0])
            print("Tu"+" "+tenirauftr[1])
            print("Il/Elle/On"+" "+tenirauftr[2])
            print("Nous"+" "+tenirauftr[3])
            print("Vous"+" "+tenirauftr[4])
            print("Ils/Elles"+" "+tenirauftr[5])

        elif verbe=="vouloir":
            print("Voici le verbe"+" "+verbe+" "+"au futur, à toutes les personnes")
            vouloirauftr=["voudrai","voudras","voudra","voudrons","voudrez","voudront"]
            print("Je"+" "+vouloirauftr[0])
            print("Tu"+" "+vouloirauftr[1])
            print("Il/Elle/On"+" "+vouloirauftr[2])
            print("Nous"+" "+vouloirauftr[3])
            print("Vous"+" "+vouloirauftr[4])
            print("Ils/Elles"+" "+vouloirauftr[5])

        elif verbe=="être":
            print("Voici le verbe"+" "+verbe+" "+"au futur, à toutes les personnes")
            êtreauftr=["serai","seras","sera","serons","serez","seront"]
            print("Je"+" "+êtreauftr[0])
            print("Tu"+" "+êtreauftr[1])
            print("Il/Elle/On"+" "+êtreauftr[2])
            print("Nous"+" "+êtreauftr[3])
            print("Vous"+" "+êtreauftr[4])
            print("Ils/Elles"+" "+êtreauftr[5])

        elif verbe=="savoir":
            print("Voici le verbe"+" "+verbe+" "+"au futur, à toutes les personnes")
            savoirauftr=["saurai","sauras","saura","saurons","saurez","sauront"]
            print("Je"+" "+savoirauftr[0])
            print("Tu"+" "+savoirauftr[1])
            print("Il/Elle/On"+" "+savoirauftr[2])
            print("Nous"+" "+savoirauftr[3])
            print("Vous"+" "+savoirauftr[4])
            print("Ils/Elles"+" "+savoirauftr[5])
#courir ou mourir
        elif verbe[-3:]=="rir":
            print("Voici le verbe"+" "+verbe+" "+"au futur, à toutes les personnes")
            print("Je"+" "+radical+"rai")
            print("Tu"+" "+radical+"ras")
            print("Il/Elle/On"+" "+radical+"ra")
            print("Nous"+" "+radical+"rons")
            print("Vous"+" "+radical+"rez")
            print("Ils/Elles"+" "+radical+"ront")

        elif verbe[-3:]=="ger":
            print("Voici le verbe"+" "+verbe+" "+"au futur, à toutes les personnes")
            if verbe[0:1] in voyelle:
                print("J'"+verbe+"ai")
            else:
                print("Je"+" "+verbe+"ai")
            print("Tu"+" "+verbe+"as")
            print("Il/Elle/On"+" "+verbe+"a")
            print("Nous"+" "+verbe+"ons")
            print("Vous"+" "+verbe+"ez")
            print("Ils/Elles"+" "+verbe+"ont")

        elif verbe[-3:]=="dre":
            print("Voici le verbe"+" "+verbe+" "+"au futur, à toutes les personnes")
            if verbe[0:1] in voyelle:
                print("J'"+verbeendre+"ai")
            else:
                print("Je"+" "+verbeendre+"ai")
            print("Tu"+" "+verbeendre+"as")
            print("Il/Elle/On"+" "+verbeendre+"a")
            print("Nous"+" "+verbeendre+"ons")
            print("Vous"+" "+verbeendre+"ez")
            print("Ils/Elles"+" "+verbeendre+"ont")

        else:
            if verbe[0:1] in voyelle:
                print("Voici le verbe"+" "+verbe+" "+"au futur, à toutes les personnes")
                print("J'"+verbe+"ai")
            else:
                print("Je"+" "+verbe+"ai")
            print("Tu"+" "+verbe+"as")
            print("Il/Elle/On"+" "+verbe+"a")
            print("Nous"+" "+verbe+"ons")
            print("Vous"+" "+verbe+"ez")
            print("Ils/Elles"+" "+verbe+"ont")

    elif réponsetemps=="passé composé":
        print("Voici le verbe"+" "+verbe+" "+"au passé composé à toutes les personnes:")
        print(" ")
        if verbe=="avoir":
            print("J'ai eu")
            print("Tu as eu")
            print("Il/Elle/On a eu")
            print("Nous avons eu")
            print("Vous avez eu")
            print("Ils/Elles ont eu")

        elif verbe=="être":
            print("J'ai été")
            print("Tu as été")
            print("Il/Elle/On a été")
            print("Nous avons été")
            print("Vous avez été")
            print("Ils/Elles ont été")

        elif verbe=="venir":
            print("Je"+" "+"suis"+" "+radical+"u(e)")
            print("Tu"+" "+"es"+" "+radical+"u(e)")
            print("Il/Elle/On"+" "+"est"+" "+radical+"u(e)(s)")
            print("Nous"+" "+"sommes"+" "+radical+"u(e)s")
            print("Vous"+" "+"êtes"+" "+radical+"u(e)s")
            print("Ils/Elles"+" "+"sont"+" "+radical+"u(e)s")

        elif verbe=="mourir":
            print("Je"+" "+"suis"+" "+"mort(e)")
            print("Tu"+" "+"es"+" "+radical+"mort(e)")
            print("Il/Elle/On"+" "+"est"+" "+radical+"mort(e)(s)")
            print("Nous"+" "+"sommes"+" "+radical+"mort(e)s")
            print("Vous"+" "+"êtes"+" "+radical+"mort(e)s")
            print("Ils/Elles"+" "+"sont"+" "+radical+"mort(e)s")

        elif verbe[-3:]=="descendre":
            print("Je"+" "+"suis"+" "+radical+"u(e)")
            print("Tu"+" "+"es"+" "+radical+"u(e)")
            print("Il/Elle/On"+" "+"est"+" "+radical+"u(e)(s)")
            print("Nous"+" "+"sommes"+" "+radical+"u(e)s")
            print("Vous"+" "+"êtes"+" "+radical+"u(e)s")
            print("Ils/Elles"+" "+"sont"+" "+radical+"u(e)s")

        elif verbe[-5:]=="endre":#prendre comprendre apprendre
            print("J'"+"ai"+" "+verbe[:-5]+"is")
            print("Tu"+" "+"as"+" "+verbe[:-5]+"is")
            print("Il/Elle/On"+" "+"a"+" "+verbe[:-5]+"is")
            print("Nous"+" "+"avons"+" "+verbe[:-5]+"is")
            print("Vous"+" "+"avez"+" "+verbe[:-5]+"is")
            print("Ils/Elles"+" "+"ont"+" "+verbe[:-5]+"is")

        else:
            auxpassé=input("Quel est l'auxiliaire de ton verbe, être ou avoir ?")
            print("Voici le verbe"+" "+verbe+" "+"au passé composé, à toutes les personnes")
            if auxpassé=="être":
                if verbe[-2:]=="er":
                    if verbe[:2]=="s'" or verbe[:2]=="se":#se laver,se doucher,s'absenter
                        vbpronominaux=verbe[2:-2]
                        print("Je"+" "+"me"+" "+"suis"+" "+vbpronominaux+"é(e)")
                        print("Tu"+" "+"t'"+"es"+" "+vbpronominaux+"é(e)")
                        print("Il/Elle/On"+" "+"s'"+"est"+" "+vbpronominaux+"é(e)(s)")
                        print("Nous"+" "+"nous"+" "+"sommes"+" "+vbpronominaux+"é(e)s")
                        print("Vous"+" "+"vous"+" "+"êtes"+" "+vbpronominaux+"é(e)s")
                        print("Ils/Elles"+" "+"se"+" "+"sont"+" "+vbpronominaux+"é(e)s")
                    else:
                        print("Je"+" "+"suis"+" "+radical+"é(e)")
                        print("Tu"+" "+"es"+" "+radical+"é(e)")
                        print("Il/Elle/On"+" "+"est"+" "+radical+"é(e)(s)")
                        print("Nous"+" "+"sommes"+" "+radical+"é(e)s")
                        print("Vous"+" "+"êtes"+" "+radical+"é(e)s")
                        print("Ils/Elles"+" "+"sont"+" "+radical+"é(e)s")

                elif verbe[-2:]=="ir":#ex partir sortir
                    if verbe[0:1] in voyelle:
                        print("J'"+radical[:-1]+"ais")
                    else:
                        print("Je"+" "+"suis"+" "+radical+"i(e)")
                        print("Tu"+" "+"es"+" "+radical+"i(e)")
                        print("Il/Elle/On"+" "+"est"+" "+radical+"i(e)(s)")
                        print("Nous"+" "+"sommes"+" "+radical+"i(e)s")
                        print("Vous"+" "+"êtes"+" "+radical+"i(e)s")
                        print("Ils/Elles"+" "+"sont"+" "+radical+"i(e)s")

                else:
                    print("Nous sommes désolés, nous ne pouvons pas conjuguer ce verbe, veuillez nous en excuser.")

            elif auxpassé=="avoir":
                if verbe[-2:]=="er":
                    print("J'"+"ai"+" "+radical+"é")
                    print("Tu"+" "+"as"+" "+radical+"é")
                    print("Il/Elle/On"+" "+"a"+" "+radical+"é")
                    print("Nous"+" "+"avons"+" "+radical+"é")
                    print("Vous"+" "+"avez"+" "+radical+"é")
                    print("Ils/Elles"+" "+"ont"+" "+radical+"é")

                elif verbe[-2:]=="ir":
                    print("J'"+"ai"+" "+radical+"i")
                    print("Tu"+" "+"as"+" "+radical+"i")
                    print("Il/Elle/On"+" "+"a"+" "+radical+"i")
                    print("Nous"+" "+"avons"+" "+radical+"i")
                    print("Vous"+" "+"avez"+" "+radical+"i")
                    print("Ils/Elles"+" "+"ont"+" "+radical+"i")

                elif verbe[-2:]=="re":#dire écrire faire
                    print("J'"+"ai"+" "+radical+"t")
                    print("Tu"+" "+"as"+" "+radical+"t")
                    print("Il/Elle/On"+" "+"a"+" "+radical+"t")
                    print("Nous"+" "+"avons"+" "+radical+"t")
                    print("Vous"+" "+"avez"+" "+radical+"t")
                    print("Ils/Elles"+" "+"ont"+" "+radical+"t")

                else:
                    print("Nous sommes désolés, nous ne pouvons pas conjuguer ce verbe, veuillez nous en excuser.")
            else:
                print("On a dit être ou avoir, réessayez !")

    elif réponsetemps=="passé simple":
        print("Voici le verbe"+" "+verbe+" "+"au passé simple à toutes les personnes:")
        print(" ")
        if verbe=="boire":
            print("Je bus")
            print("Tu bus")
            print("Il/Elle/On but")
            print("Nous bûmes")
            print("Vous bûtes")
            print("Ils/Elles burent")

        elif verbe=="avoir":
            print("J'eus")
            print("Tu eus")
            print("Il/Elle/On eut")
            print("Nous eûmes")
            print("Vous eûtes")
            print("Ils/Elles eurent")

        elif verbe=="être":
            print("Je fus")
            print("Tu fus")
            print("Il/Elle fut")
            print("Nous fûmes")
            print("Vous fûtes")
            print("Ils furent")

        elif verbe=="faire":
            print("Je fis")
            print("Tu fis")
            print("Il/Elle fit")
            print("Nous fîmes")
            print("Vous fîtes")
            print("Ils firent")

        elif verbe=="naître":
            print("Je naquis")
            print("Tu naquis")
            print("Il/Elle/On naquit")
            print("Nous naquîmes")
            print("Vous naquîtes")
            print("Ils/Elles naquirent")

        elif verbe=="mourir":
            print("Je mourus")
            print("Tu mourus")
            print("Il/Elle/On mourut")
            print("Nous mourûmes")
            print("Vous mourûtes")
            print("Ils/Elles moururent")

        elif verbe=="voir":
            print("Je vis")
            print("Tu vit")
            print("Il/Elle/On vit")
            print("Nous vîmes")
            print("Vous vîtes")
            print("Ils/Elles virent")

        elif verbe[-4:]=="enir":#ex venir tenir
            if verbe[0:1] in voyelle:
                print("J'"+radical[:-2]+"ins")
            else:
                print("Je"+" "+radical[:-2]+"ins")
            print("Tu"+" "+radical[:-2]+"ins")
            print("Il/Elle/On"+" "+radical[:-2]+"int")
            print("Nous"+" "+radical[:-2]+"înmes")
            print("Vous"+" "+radical[:-2]+"întes")
            print("Ils/Elles"+" "+radical[:-2]+"inrent")
        
        elif verbe[-3:]=="ger":
            print("Voici le verbe"+" "+verbe+" "+"au futur, à toutes les personnes")
            if verbe[0:1] in voyelle:
                print("J'"+verbe+"ai")
            else:
                print("Je"+" "+radical+"eai")
            print("Tu"+" "+radical+"eas")
            print("Il/Elle/On"+" "+radical+"ea")
            print("Nous"+" "+radical+"eâmes")
            print("Vous"+" "+radical+"eâtes")
            print("Ils/Elles"+" "+radical+"èrent")
        
        elif verbe[-2:]=="er":
            if verbe[0:1] in voyelle:
                print("J'"+radical+"ai")
            else:
                print("Je"+" "+radical+"ai")
            print("Tu"+" "+radical+"as")
            print("Il/Elle/On"+" "+radical+"a")
            print("Nous"+" "+radical+"âmes")
            print("Vous"+" "+radical+"âtes")
            print("Ils/Elles"+" "+radical+"èrent")
        else:
            if verbe[0:1] in voyelle:
                print("J'"+radical+"is")
            else:
                print("Je"+" "+radical+"is")
            print("Tu"+" "+radical+"is")
            print("Il/Elle/On"+" "+radical+"it")
            print("Nous"+" "+radical+"îmes")
            print("Vous"+" "+radical+"îtes")
            print("Ils/Elles"+" "+radical+"irent")
    
    else:
        print("Ce n'est pas un temps veuillez réessayer avec : passé composé,passé simple,imparfait,présent,ou futur !")
