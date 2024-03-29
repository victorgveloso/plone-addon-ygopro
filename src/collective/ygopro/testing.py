# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.ygopro


class CollectiveYgoproLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.ygopro)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.ygopro:default')


COLLECTIVE_YGOPRO_FIXTURE = CollectiveYgoproLayer()


COLLECTIVE_YGOPRO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_YGOPRO_FIXTURE,),
    name='CollectiveYgoproLayer:IntegrationTesting',
)


COLLECTIVE_YGOPRO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_YGOPRO_FIXTURE,),
    name='CollectiveYgoproLayer:FunctionalTesting',
)


COLLECTIVE_YGOPRO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_YGOPRO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveYgoproLayer:AcceptanceTesting',
)
