# -*- coding: utf-8 -*-
#
# Copyright (C) 2007 Edgewall Software
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://babel.edgewall.org/wiki/License.
#
# This software consists of voluntary contributions made by many
# individuals. For the exact contribution history, see the revision
# history and logs, available at http://babel.edgewall.org/log/.

PLURALS = {
    # Afrikaans - From Pootle's PO's
    'af': (2, '(n != 1)'),
    # Arabic - From Pootle's PO's
    'ar': (6, '(n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n>=3 && n<=10 ? 3 : n>=11 && n<=99 ? 4 : 5)'),
    # Bulgarian - From Pootle's PO's
    'bg': (2, '(n != 1)'),
    # Bengali - From Pootle's PO's
    'bn': (2, '(n != 1)'),
    # Catalan - From Pootle's PO's
    'ca': (2, '(n != 1)'),
    # Czech
    'cs': (3, '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)'),
    # Danish
    'da': (2, '(n != 1)'),
    # German
    'de': (2, '(n != 1)'),
    # Greek
    'el': (2, '(n != 1)'),
    # English
    'en': (2, '(n != 1)'),
    # Esperanto
    'eo': (2, '(n != 1)'),
    # Spanish
    'es': (2, '(n != 1)'),
    # Estonian
    'et': (2, '(n != 1)'),
    # Basque - From Pootle's PO's
    'eu': (2, '(n != 1)'),
    # Persian - From Pootle's PO's
    'fa': (1, '0'),
    # Finnish
    'fi': (2, '(n != 1)'),
    # French
    'fr': (2, '(n > 1)'),
    # Furlan - From Pootle's PO's
    'fur': (2, '(n > 1)'),
    # Irish
    'ga': (3, 'n==1 ? 0 : n==2 ? 1 : 2'),
    # Galego - From Pootle's PO's
    'gl': (2, '(n != 1)'),
    # Hausa - From Pootle's PO's
    'ha': (2, '(n != 1)'), 
    # Hebrew
    'he': (2, '(n != 1)'),
    # Hindi - From Pootle's PO's
    'hi': (2, '(n != 1)'), 
    # Croatian
    'hr': (3, '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)'),
    # Hungarian
    'hu': (1, '0'),
    # Armenian - From Pootle's PO's
    'hy': (1, '0'),
    # Icelandic - From Pootle's PO's
    'is': (2, '(n != 1)'),
    # Italian
    'it': (2, '(n != 1)'),
    # Japanese
    'ja': (1, '0'),
    # Georgian - From Pootle's PO's
    'ka': (1, '0'),
    # Kongo - From Pootle's PO's
    'kg': (2, '(n != 1)'),
    # Khmer - From Pootle's PO's
    'km': (1, '0'),
    # Korean
    'ko': (1, '0'),
    # Kurdî - From Pootle's PO's
    'ku': (2, '(n != 1)'),
    # Lithuanian
    'lt': (3, '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : 2)'),
    # Latvian
    'lv': (3, '(n%10==1 && n%100!=11 ? 0 : n != 0 ? 1 : 2)'),
    # Maltese - From Pootle's PO's
    'mt': (4, '(n==1 ? 0 : n==0 || ( n%100>1 && n%100<11) ? 1 : (n%100>10 && n%100<20 ) ? 2 : 3)'),
    # Norwegian Bokmal
    'nb': (2, '(n != 1)'),
    # Dutch
    'nl': (2, '(n != 1)'),
    # Norwegian Nynorsk
    'nn': (2, '(n != 1)'),
    # Norwegian
    'no': (2, '(n != 1)'),
    # Punjabi - From Pootle's PO's
    'pa': (2, '(n != 1)'),
    # Polish
    'pl': (3, '(n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)'),
    # Portuguese
    'pt': (2, '(n != 1)'),
    # Brazilian
    'pt_BR': (2, '(n > 1)'),
    # Romanian - From Pootle's PO's
    'ro': (3, '(n==1 ? 0 : (n==0 || (n%100 > 0 && n%100 < 20)) ? 1 : 2)'),
    # Russian
    'ru': (3, '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)'),
    # Slovak
    'sk': (3, '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)'),
    # Slovenian
    'sl': (4, '(n%100==1 ? 0 : n%100==2 ? 1 : n%100==3 || n%100==4 ? 2 : 3)'),
    # Serbian - From Pootle's PO's
    'sr': (3, '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10< =4 && (n%100<10 || n%100>=20) ? 1 : 2)'),
    # Sesotho - From Pootle's PO's
    'st': (2, '(n != 1)'),
    # Swedish
    'sv': (2, '(n != 1)'),
    # Turkish
    'tr': (1, '0'),
    # Ukrainian
    'uk': (3, '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)'),
    # Venda - From Pootle's PO's
    've': (2, '(n != 1)'),
    # Vietnamese - From Pootle's PO's
    'vi': (1, '0'),
    # Xhosa - From Pootle's PO's
    'xh': (2, '(n != 1)'),
    # Chinese - From Pootle's PO's
    'zh_CN': (1, '0'),
    'zh_HK': (1, '0'),
    'zh_TW': (1, '0'),
}
