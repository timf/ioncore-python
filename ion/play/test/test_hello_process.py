#!/usr/bin/env python

"""
@file ion/play/test/test_hello_process.py
@test ion.play.hello_process Example unit tests for sample code.
@author David Stuebe
"""
import ion.util.ionlog
log = ion.util.ionlog.getLogger(__name__)

from twisted.internet import defer

from ion.play.hello_process import HelloProcessClient
from ion.test.iontest import IonTestCase

from ion.core.process.process import ProcessDesc
from ion.core import bootstrap

class HelloProcessTest(IonTestCase):
    """
    Testing example hello service.
    """

    @defer.inlineCallbacks
    def setUp(self):
        yield self._start_container()

    @defer.inlineCallbacks
    def tearDown(self):
        yield self._stop_container()

    @defer.inlineCallbacks
    def test_hello(self):


        pd1 = {'name':'hello1','module':'ion.play.hello_process','class':'HelloProcess'}

        proc1 = ProcessDesc(**pd1)


        sup1 = yield bootstrap.create_supervisor()
        
        proc1_id = yield self.test_sup.spawn_child(proc1)

        sup2 = yield bootstrap.create_supervisor()
        
        
        log.info('Calling hello there with hc(sup1)')
        hc1 = HelloProcessClient(proc=sup1,target=proc1_id)
        yield hc1.hello("Hi there, hello1")


        log.info('Calling hello there with hc(sup2)')
        hc2 = HelloProcessClient(proc=sup2,target=proc1_id)
        yield hc2.hello("Hi there, hello2")


        log.info('Tada!')
