def get_rules(transactions,apriori_result):
    for i in range(1,len(apriori_result)):
        for element in apriori_result[i]:
            for item in element:
                print tuple([item]), ' => ', tuple(set(element).difference(item))
                freq = countFrequencies(transactions,[tuple([item]),element])
                print 'conf:',freq[element]*100.0/freq[tuple([item])],'%'
