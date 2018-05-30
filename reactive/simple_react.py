from charms.reactive import when, when_not, set_state
from charmhelpers.core.hookenv import status_set

@when_not('simple-react.installed')
def install_simple_react():
    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #
    print(" -Set state Installed")
    set_state('simple-react.installed')

    print(" -Set status to active and message to Ready")
    charmhelpers.core.hookenv.status_set('active', 'Ready')