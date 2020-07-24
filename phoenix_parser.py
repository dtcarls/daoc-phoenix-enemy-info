import requests
import urllib.parse
from bs4 import BeautifulSoup
from collections import namedtuple


class PhoenixParser:
    def __init__(self, name):
        self.search_for = name

        self.player_url = "https://herald.playphoenix.online/c"
        self.guild_url = "https://herald.playphoenix.online/g"
        self.info = {}

        self.mapping = {}
        self.mapping[1] = "rp_all_time_amount"
        self.mapping[2] = "rp_all_time_server"
        self.mapping[3] = "rp_all_time_realm"
        self.mapping[4] = "rp_all_time_class"

        self.mapping[6] = "rp_last_week_amount"
        self.mapping[7] = "rp_last_week_server"
        self.mapping[8] = "rp_last_week_realm"
        self.mapping[9] = "rp_last_week_class"

        self.mapping[11] = "rp_this_week_amount"
        self.mapping[12] = "rp_this_week_server"
        self.mapping[13] = "rp_this_week_realm"
        self.mapping[14] = "rp_this_week_class"

        self.mapping[16] = "rp_last_48h_amount"
        self.mapping[17] = "rp_last_48h_server"
        self.mapping[18] = "rp_last_48h_realm"
        self.mapping[19] = "rp_last_48h_class"

        self.mapping[21] = "db_all_time_amount"
        self.mapping[22] = "db_all_time_server"
        self.mapping[23] = "db_all_time_realm"
        self.mapping[24] = "db_all_time_class"

        self.mapping[26] = "db_last_week_amount"
        self.mapping[27] = "db_last_week_server"
        self.mapping[28] = "db_last_week_realm"
        self.mapping[29] = "db_last_week_class"

        self.mapping[31] = "db_this_week_amount"
        self.mapping[32] = "db_this_week_server"
        self.mapping[33] = "db_this_week_realm"
        self.mapping[34] = "db_this_week_class"

        self.mapping[36] = "db_last_48h_amount"
        self.mapping[37] = "db_last_48h_server"
        self.mapping[38] = "db_last_48h_realm"
        self.mapping[39] = "db_last_48h_class"

        self.mapping[41] = "death_all_time_amount"
        self.mapping[42] = "death_all_time_server"
        self.mapping[43] = "death_all_time_realm"
        self.mapping[44] = "death_all_time_class"

        self.mapping[46] = "death_last_week_amount"
        self.mapping[47] = "death_last_week_server"
        self.mapping[48] = "death_last_week_realm"
        self.mapping[49] = "death_last_week_class"

        self.mapping[51] = "death_this_week_amount"
        self.mapping[52] = "deaht_this_week_server"
        self.mapping[53] = "deaht_this_week_realm"
        self.mapping[54] = "death_this_week_class"

        self.mapping[56] = "death_last_48h_amount"
        self.mapping[57] = "death_last_48h_server"
        self.mapping[58] = "death_last_48h_realm"
        self.mapping[59] = "death_last_48h_class"

        self.mapping[61] = "kills_all_time_amount"
        self.mapping[62] = "kills_all_time_server"
        self.mapping[63] = "kills_all_time_realm"
        self.mapping[64] = "kills_all_time_class"

        self.mapping[66] = "kills_last_week_amount"
        self.mapping[67] = "kills_last_week_server"
        self.mapping[68] = "kills_last_week_realm"
        self.mapping[69] = "kills_last_week_class"

        self.mapping[71] = "kills_this_week_amount"
        self.mapping[72] = "kills_this_week_server"
        self.mapping[73] = "kills_this_week_realm"
        self.mapping[74] = "kills_this_week_class"

        self.mapping[76] = "kills_last_48h_amount"
        self.mapping[77] = "kills_last_48h_server"
        self.mapping[78] = "kills_last_48h_realm"
        self.mapping[79] = "kills_last_48h_class"

        self.mapping[81] = "solokills_all_time_amount"
        self.mapping[82] = "solokills_all_time_server"
        self.mapping[83] = "solokills_all_time_realm"
        self.mapping[84] = "solokills_all_time_class"

        self.mapping[86] = "solokills_last_week_amount"
        self.mapping[87] = "solokills_last_week_server"
        self.mapping[88] = "solokills_last_week_realm"
        self.mapping[89] = "solokills_last_week_class"

        self.mapping[91] = "solokills_this_week_amount"
        self.mapping[92] = "solokills_this_week_server"
        self.mapping[93] = "solokills_this_week_realm"
        self.mapping[94] = "solokills_this_week_class"

        self.mapping[96] = "solokills_last_48h_amount"
        self.mapping[97] = "solokills_last_48h_server"
        self.mapping[98] = "solokills_last_48h_realm"
        self.mapping[99] = "solokills_last_48h_class"

        self.mapping[101] = "kills_by_realm_all_time_alb"
        self.mapping[102] = "kills_by_realm_all_time_mid"
        self.mapping[103] = "kills_by_realm_all_time_hib"

        self.mapping[105] = "kills_by_realm_last_week_alb"
        self.mapping[106] = "kills_by_realm_last_week_mid"
        self.mapping[107] = "kills_by_realm_last_week_hib"

        self.mapping[109] = "kills_by_realm_this_week_alb"
        self.mapping[110] = "kills_by_realm_this_week_mid"
        self.mapping[111] = "kills_by_realm_this_week_hib"

        self.mapping[113] = "kills_by_realm_last_48h_alb"
        self.mapping[114] = "kills_by_realm_last_48h_mid"
        self.mapping[115] = "kills_by_realm_last_48h_hib"

        try:
            self.get_html_from_herald()
            self.get_player_info()
            self.fix_player_data()
            self.get_all_stats()
            self.get_last_updated()
            self.info['player_url'] = "{}/{}".format(
                self.player_url, urllib.parse.quote_plus(self.info['player_name']))
            self.info['guild_url'] = "{}/{}".format(
                self.guild_url, urllib.parse.quote_plus(self.info['player_guild']))
            self.info = self.info_to_object()
        except:
            raise Exception("Unable to parse data for: {}".format(
                self.search_for))

    def get_html_from_herald(self):
        url = "{}/{}".format(self.player_url, self.search_for)
        r = requests.get(url)
        if r.status_code < 299:
            soup = BeautifulSoup(r.content, 'html.parser')
            html = list(soup.children)[2]
            self.body = list(html.children)[3]
        else:
            raise Exception("Something went wrong when fetching {}".format(
                url))

    def info_to_object(self):
        return namedtuple('Struct', self.info.keys())(*self.info.values())

    def get_last_updated(self):
        count = 0
        for aside in list(self.body.find_all('aside')[0]):
            if len(aside) > 0:
                if count == 46:
                    self.info['last_updated'] = aside.strip()
                    return
            count = count + 1

    def get_player_info(self):
        try:
            (self.info['player_name'],
             _,
             self.info['player_guild'],
             _,
             self.info['player_class'],
             _,
             _,
             _,
             self.info['player_level'],
             _,
             _,
             _,
             self.info['player_rr'],
             _,
             _,
             _,
             self.info['player_race'],
             _,
             self.info['player_pretty_rr']) = self.body.find('div') \
                .get_text().strip().split("\n")
        except:
            raise Exception("Unable to parse player data for: {}".format(
                self.search_for))

    def get_all_stats(self):
        count = 0
        for td in list(self.body.find_all('td')):
            if len(td) > 0:
                if count in range(1, 100):
                    if count % 5 != 0:
                        self.info[self.mapping[count]] = td.get_text()
                if count in range(100, 115):
                    if count % 4 != 0:
                        self.info[self.mapping[count]] = td.get_text()
                count = count + 1
        self.get_realm_by_class()

    def fix_player_data(self):
        for row in self.info:
            self.info[row] = self.info[row].strip()
            if row == "player_rr":
                self.info[row] = self.info[row].strip("Realm Rank ")
            if row == "player_level":
                self.info[row] = self.info[row].strip("Level ")
            if row == "player_guild":
                self.info[row] = self.info[row].replace(">", "")
                self.info[row] = self.info[row].replace("<", "")

    def get_realm_by_class(self):
        mid = [
            "Berserker",
            "Bonedancer",
            "Healer",
            "Hunter",
            "Runemaster",
            "Savage",
            "Shadowblade",
            "Shaman",
            "Skald",
            "Spiritmaster",
            "Thane",
            "Warrior"
        ]

        hib = [
            "Animist",
            "Bard",
            "Blademaster",
            "Champion",
            "Druid",
            "Eldritch",
            "Enchanter",
            "Enchantress",
            "Hero",
            "Heroine",
            "Mentalist",
            "Nightshade",
            "Ranger",
            "Valewalker",
            "Warden",
        ]

        alb = [
            "Armsman",
            "Armswoman",
            "Cabalist",
            "Cleric",
            "Friar",
            "Infiltrator",
            "Mercenary",
            "Minstrel",
            "Necromancer",
            "Paladin",
            "Reaver",
            "Scout",
            "Sorcerer",
            "Sorceress",
            "Theurgist",
            "Wizard",
        ]

        if self.info['player_class'] in mid:
            self.info['player_realm'] = "Mid"
            self.info['realm_color'] = 0x4A90E2
        if self.info['player_class'] in hib:
            self.info['player_realm'] = "Hib"
            self.info['realm_color'] = 0x7ED321
        if self.info['player_class'] in alb:
            self.info['player_realm'] = "Alb"
            self.info['realm_color'] = 0xD0021B