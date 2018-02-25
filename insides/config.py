"""
_______________.___.
\______   \__  |   |
 |    |  _//   |   |
 |    |   \\____   |
 |______  // ______|
        \/ \/       
   _____         _______           ________        __________.__         ._____________   __________ 
  /  _  \   ____ \   _  \   ____   \_____  \___  __\______   |  |   ____ |__\__    _______\______   \
 /  /_\  \ /    \/  /_\  \ /    \    _(__  <\  \/  /|     ___|  |  /  _ \|  | |    |_/ __ \|       _/
/    |    |   |  \  \_/   |   |  \  /       \>    < |    |   |  |_(  <_> |  | |    |\  ___/|    |   \
\____|__  |___|  /\_____  |___|  / /______  /__/\_ \|____|   |____/\____/|__| |____| \___  |____|_  /
        \/     \/       \/     \/         \/      \/                                     \/       \/ 

                                ~ Changing Coder Name Wont Make You One :)
                                             ~ An0n 3xPloiTeR :)
"""

from colors import *

"""
------------------------------------------------------------------
						Default Vars
------------------------------------------------------------------
"""

website = "http://www.animegg.org"
__prog_version = "1.0 {{beta}}"

"""
------------------------------------------------------------------
						Optparse Variables
------------------------------------------------------------------
"""

_usage 		= "\r{}[{}#{}] Usage: python {}%prog{} --noshit {}http://animegg.org/series/bleach".format(w,c,w,g,w,g)
_version 	= "{}[{}~{}] {}Version: {}1.0 {{beta}}".format(w,c,w,w,g)

"""
------------------------------------------------------------------
						Headers Dict's
------------------------------------------------------------------
"""

__common_headers 	  = {
    'X-XSS-Protection'          	: 'Tries To Prevent XSS', 
    'Strict-Transport-Security' 	: 'Forces Redirecting Traffic Through HTTPS',
    'X-Frame-Options'           	: 'Prevents Clickjacking',
    'X-Content-Type-Options'    	: 'Prevents MIME Types Security Risks',
	'Access-Control-Allow-Origin'	: 'Prevents CORS',
    'Content-Security-Policy'   	: 'Prevents XSS, RCE && Clickjacking'
}

__interesting_headers = {
	'X-Powered-By'					: 'Programming Language',
	'Server'						: 'Web Server',
	'CF-RAY'						: 'Cloudflare',	
	'X-AspNet-Version'				: 'ASP.Net Framework',
	'laravel_session'				: 'Laravel Framework',
	'X-Pingback'					: 'Wordpress CMS',
	'X-XSS-Protection'				: 'Tries To Prevent XSS',
	'X-Frame-Options'				: 'Prevents Clickjacking',
	'Content-Security-Policy'		: 'Prevents XSS & Other Attacks',
	'Access-Control-Allow-Origin'	: 'Prevents CORS'
}

# """
# ------------------------------------------------------------------
# 						Plugins Lists
# ------------------------------------------------------------------
# """

# _plugs 	= {
# 	'akismet'				: 'LICENSE.txt',
# 	'better-wp-security'	: 'readme.txt',
# }