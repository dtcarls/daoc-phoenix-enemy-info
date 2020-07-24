#!/usr/bin/env python3


class RealmRanks:
    def __init__(self, rank=False, rp=False):
        self.realmrank = rank
        self.current_rp = rp

        self.r1l1 = 0
        self.r1l2 = 25
        self.r1l3 = 125
        self.r1l4 = 350
        self.r1l5 = 750
        self.r1l6 = 1375
        self.r1l7 = 2275
        self.r1l8 = 3500
        self.r1l9 = 5100

        self.r2l0 = 7125
        self.r2l1 = 9625
        self.r2l2 = 12650
        self.r2l3 = 16250
        self.r2l4 = 20475
        self.r2l5 = 25375
        self.r2l6 = 31000
        self.r2l7 = 37400
        self.r2l8 = 44625
        self.r2l9 = 52725

        self.r3l0 = 61750
        self.r3l1 = 71750
        self.r3l2 = 82750
        self.r3l3 = 94875
        self.r3l4 = 108100
        self.r3l5 = 122500
        self.r3l6 = 138125
        self.r3l7 = 155025
        self.r3l8 = 173250
        self.r3l9 = 192850

        self.r4l0 = 213875
        self.r4l1 = 236375
        self.r4l2 = 286000
        self.r4l3 = 313225
        self.r4l4 = 342125
        self.r4l5 = 372750
        self.r4l6 = 405150
        self.r4l7 = 439375
        self.r4l8 = 439375
        self.r4l9 = 475475

        self.r5l0 = 513500
        self.r5l1 = 553500
        self.r5l2 = 595525
        self.r5l3 = 639625
        self.r5l4 = 685850
        self.r5l5 = 734259
        self.r5l6 = 784875
        self.r5l7 = 837775
        self.r5l8 = 893000
        self.r5l9 = 950600

        self.r6l0 = 1010625
        self.r6l1 = 1073125
        self.r6l2 = 1138150
        self.r6l3 = 1205750
        self.r6l4 = 1275975
        self.r6l5 = 1348875
        self.r6l6 = 1424500
        self.r6l7 = 1502900
        self.r6l8 = 1584125
        self.r6l9 = 1668225

        self.r7l0 = 1755250
        self.r7l1 = 1845250
        self.r7l2 = 1938275
        self.r7l3 = 2034375
        self.r7l4 = 2133600
        self.r7l5 = 2236000
        self.r7l6 = 2341625
        self.r7l7 = 2450525
        self.r7l8 = 2562750
        self.r7l9 = 2678350

        self.r8l0 = 2797375
        self.r8l1 = 2919875
        self.r8l2 = 3045900
        self.r8l3 = 3175500
        self.r8l4 = 3308725
        self.r8l5 = 3445625
        self.r8l6 = 3586250
        self.r8l7 = 3730650
        self.r8l8 = 3878875
        self.r8l9 = 4030975

        self.r9l0 = 4187000
        self.r9l1 = 4347000
        self.r9l2 = 4511025
        self.r9l3 = 4679125
        self.r9l4 = 4851350
        self.r9l5 = 5027750
        self.r9l6 = 5208375
        self.r9l7 = 5393275
        self.r9l8 = 5582500
        self.r9l9 = 5776100

        self.r10l0 = 5974125
        self.r10l1 = 6176625
        self.r10l2 = 6383650
        self.r10l3 = 6595250
        self.r10l4 = 6811475
        self.r10l5 = 7032375
        self.r10l6 = 7258000
        self.r10l7 = 7488400
        self.r10l8 = 7723625
        self.r10l9 = 7963725

        self.r11l0 = 8208750
        self.r11l1 = 9111713
        self.r11l2 = 10114001
        self.r11l3 = 11226541
        self.r11l4 = 12461460
        self.r11l5 = 13832221
        self.r11l6 = 15353765
        self.r11l7 = 17042680
        self.r11l8 = 18917374
        self.r11l9 = 20998286

        self.r12l0 = 23308097
        self.r12l1 = 25871988
        self.r12l2 = 28717906
        self.r12l3 = 31876876
        self.r12l4 = 35383333
        self.r12l5 = 39275499
        self.r12l6 = 43595804
        self.r12l7 = 48391343
        self.r12l8 = 53714390
        self.r12l9 = 59622973

        self.r13l0 = 66181501
        self.r13l1 = 73461466
        self.r13l2 = 81542227
        self.r13l3 = 90511872
        self.r13l4 = 100468178
        self.r13l5 = 111519678
        self.r13l6 = 123786843
        self.r13l7 = 137403395
        self.r13l8 = 152517769
        self.r13l9 = 169294723

        self.r14l0 = 187917143

        self.get_realmrank()

    def get_realmrank(self):
        (rank, level) = self.realmrank.split("L")
        rank = int(rank)
        level = int(level)
        if rank >= 14:
            rank = 14
            level = 0

        self.rank = rank
        self.level = level

        return getattr(self, "r{}l{}".format(rank, level))

    def get_rank(self):
        return self.rank

    def get_level(self):
        return self.level

    def next_level(self, pretty=False):
        rank = self.rank
        level = self.level

        if rank == 14:
            level = 0
        elif level < 9:
            level = level + 1
        else:
            level = 0
            rank = rank + 1

        next_level_pretty = "r{}l{}".format(rank, level)
        next_level = getattr(self, next_level_pretty)
        if pretty:
            return next_level_pretty.upper()
        else:
            return "{:,}".format(next_level - self.current_rp)

    def next_rank(self, pretty=False):
        level = self.get_level()
        rank = self.get_rank()

        if rank == 14:
            rank = 14
        else:
            rank = rank + 1
        level = 0

        next_rank_pretty = "r{}l{}".format(rank, level)
        next_rank = getattr(self, next_rank_pretty)
        if pretty:
            return next_rank_pretty.upper()
        else:
            return "{:,}".format(next_rank - self.current_rp)

    def set_rp(self, rp):
        self.current_rp = rp