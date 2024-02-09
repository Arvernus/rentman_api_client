from enum import Enum


class StockLocationItemputResponseSchemaDataCountry(str, Enum):
    AF = "af"
    AL = "al"
    DZ = "dz"
    AD = "ad"
    AO = "ao"
    AI = "ai"
    AR = "ar"
    AM = "am"
    AW = "aw"
    AU = "au"
    AT = "at"
    AZ = "az"
    BS = "bs"
    BH = "bh"
    BD = "bd"
    BB = "bb"
    BY = "by"
    BE = "be"
    BZ = "bz"
    BJ = "bj"
    BM = "bm"
    BT = "bt"
    BO = "bo"
    BQ = "bq"
    BA = "ba"
    BW = "bw"
    BR = "br"
    BN = "bn"
    BG = "bg"
    KH = "kh"
    CM = "cm"
    CA = "ca"
    KY = "ky"
    CL = "cl"
    CN = "cn"
    CO = "co"
    CD = "cd"
    CG = "cg"
    CR = "cr"
    HR = "hr"
    CU = "cu"
    CW = "cw"
    CY = "cy"
    CZ = "cz"
    DK = "dk"
    DJ = "dj"
    DO = "do"
    EC = "ec"
    EG = "eg"
    SV = "sv"
    GQ = "gq"
    EE = "ee"
    ET = "et"
    FO = "fo"
    FJ = "fj"
    FI = "fi"
    FR = "fr"
    GF = "gf"
    PF = "pf"
    GA = "ga"
    GE = "ge"
    DE = "de"
    GH = "gh"
    GR = "gr"
    GD = "gd"
    GP = "gp"
    GU = "gu"
    GT = "gt"
    GN = "gn"
    GY = "gy"
    HT = "ht"
    HN = "hn"
    HK = "hk"
    HU = "hu"
    IS_ = "is"
    IN_ = "in"
    ID = "id"
    IR = "ir"
    IQ = "iq"
    IE = "ie"
    IM = "im"
    IL = "il"
    IT = "it"
    CI = "ci"
    JM = "jm"
    JP = "jp"
    JO = "jo"
    KZ = "kz"
    KE = "ke"
    KI = "ki"
    XK = "xk"
    KW = "kw"
    KG = "kg"
    LA = "la"
    LV = "lv"
    LB = "lb"
    LS = "ls"
    LR = "lr"
    LI = "li"
    LT = "lt"
    LU = "lu"
    MO = "mo"
    MK = "mk"
    MG = "mg"
    MY = "my"
    MV = "mv"
    ML = "ml"
    MT = "mt"
    MQ = "mq"
    MR = "mr"
    MU = "mu"
    MX = "mx"
    MD = "md"
    MC = "mc"
    MN = "mn"
    ME = "me"
    MA = "ma"
    MZ = "mz"
    NA = "na"
    NP = "np"
    AN = "an"
    NC = "nc"
    NZ = "nz"
    NI = "ni"
    NG = "ng"
    VALUE_False = "False"
    OM = "om"
    PK = "pk"
    PS = "ps"
    PA = "pa"
    PG = "pg"
    PY = "py"
    PE = "pe"
    PH = "ph"
    PL = "pl"
    PT = "pt"
    PR = "pr"
    QA = "qa"
    RE = "re"
    RO = "ro"
    RU = "ru"
    RW = "rw"
    VC = "vc"
    SM = "sm"
    SA = "sa"
    SN = "sn"
    RS = "rs"
    SC = "sc"
    SG = "sg"
    SK = "sk"
    SI = "si"
    SO = "so"
    ZA = "za"
    KR = "kr"
    SS = "ss"
    ES = "es"
    LK = "lk"
    MF = "mf"
    SX = "sx"
    SD = "sd"
    SR = "sr"
    SJ = "sj"
    SZ = "sz"
    SE = "se"
    CH = "ch"
    SY = "sy"
    TW = "tw"
    TZ = "tz"
    TH = "th"
    NL = "nl"
    TG = "tg"
    TT = "tt"
    TN = "tn"
    TR = "tr"
    TC = "tc"
    US = "us"
    UG = "ug"
    UA = "ua"
    AE = "ae"
    GB = "gb"
    UY = "uy"
    UZ = "uz"
    VU = "vu"
    VA = "va"
    VE = "ve"
    VN = "vn"
    VI = "vi"
    ZM = "zm"
    ZW = "zw"

    def __str__(self) -> str:
        return str(self.value)
