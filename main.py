'''main entry'''

from optparse import *

from logger.logger import loggerHandler
from fileparser.fileExtractor import *
from trainingAlg.classifierModel import *
from trainingAlg.NaiveBayseClassifier import *

import matplotlib.pyplot as plt

#third party libs
#from daemon import Daemon

'''
class TDaemon(Daemon):
    def __init__(self, *args, **kwargs):
        super(TDaemon, self).__init__(*args, **kwargs)
        loggerHandler.debug('init deamon')

    def run(self):
        while True:
            # read file
            
            loggerHandler.debug('daemon is running...')
            time.sleep(3)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg in ('start', 'stop', 'restart'):
            d = TDaemon('testing_daemon.pid', verbose=0)
            getattr(d, arg)()
'''

def main():
    parser = OptionParser()
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Be more verbose")
    parser.add_option("-f", "--file", metavar="FILE", dest="filename", default="", help="Parse the file or zip")
    parser.add_option("-t", "--train", metavar="PATH", dest="train", help="Redo train algorithm by the special path, and will generate new example data."
                                                                             "[don't recommand to use this option for user]")


    (options, args) = parser.parse_args()
    if options.verbose:
        loggerHandler.setLevel(True)

    #options.filename = './trainingdata/authentication_failed/test.log'

    #if options.filename:
        #print "--> Parsing Jabber logs from: %s" % options.filename
        #parse the file or zip


    if options.train:
        # model = classifierModel()
        # allFeatures, featureForSampleList, labelList = model.createClassifierModel(options.train)
        # print(allFeatures)
        # dataSet = [model.setDataToVector(numericalVec, allFeatures) for numericalVec in featureForSampleList]
        #
        # clf = NaiveBayseClassifier()
        # condProb, clsProb = clf.train(dataSet, labelList)
        # print(clsProb)

        # test different single sample
        #options.filename = './trainingdata/authentication_failed/enta.jabberqa_impservice.log'
        #options.filename = './trainingdata/network_connection/enta_edgedetection403.log'
        #options.filename = './trainingdata/no_srv_record/1.log'
        options.filename = '/Users/maodanping/Downloads/20170824_155743_Jabber-Android-2017-08-24_12h08m-LOGS.zip'
        fileHandler = fileExtractor()
        featureForSample, detailedInfoList = fileHandler.logFilesProcess(options.filename)
        print(featureForSample)
        print(detailedInfoList)
        #numericalVec = model.setDataToVector(featureForSample, allFeatures)
        #print(numericalVec)
        #print(detailedInfoList)
        #print(clf.classify(numericalVec, condProb, clsProb))


        #test all the case which is trained before

        # error = 0
        # for test_samples, test_cls in zip(featureForSampleList, labelList):
        #     if test_cls != 'no_srv_record':
        #         continue
        #
        #     print(test_samples)
        #     print(test_cls)
        #     print(allFeatures)
        #     test_data = model.setDataToVector(test_samples, allFeatures)
        #     print(test_data)
        #     pred_cls = clf.classify(test_data, condProb, clsProb)
        #     if test_cls != pred_cls:
        #         print('Predict: {} -- Actual: {}'.format(pred_cls, test_cls))
        #         error += 1
        #     else:
        #         print('matchd. {}'.format(pred_cls))
        # print('Error Rate: {}'.format(error / len(test_cls)))

        #show the probabilities for classes
        # print(allFeatures)
        # fig = plt.figure()
        # ax = fig.add_subplot(111)
        # for cls, probs in condProb.items():
        #     #print(type(probs))
        #     #print(probs)
        #
        #     print(probs * clsProb[cls])
        #     print(clsProb[cls])
        #     ax.scatter(np.arange(0, len(probs)),
        #                probs * clsProb[cls],
        #                label=cls,
        #                alpha=0.3)
        #     #ax.legend()
        #     ax.legend(loc='upper center',
        #               bbox_to_anchor=(0.5,  # horizontal
        #                               1.15),  # vertical
        #               ncol=3, fancybox=True)
        # #plt.legend(loc='upper right', framealpha=0.1)

        # printedFeatures = [ feature[-25: -1] for feature in allFeatures]
        #
        # plt.xticks(np.arange(0, len(probs)), [r'$%s$'%printedFeatures[0],r'$%s$'%printedFeatures[1],r'$%s$'%printedFeatures[2],r'$%s$'%printedFeatures[3],
        #            r'$%s$'%printedFeatures[4], r'$%s$'%printedFeatures[5], r'$%s$'%printedFeatures[6], r'$%s$'%printedFeatures[7],
        #            r'$%s$'%printedFeatures[8],r'$%s$'%printedFeatures[9],r'$%s$'%printedFeatures[10]], fontsize=6, rotation=40)
        #
        # #plt.xticks(np.arange(0, len(probs)), (r'$%s$' % allFeatures[0]))
        # plt.show()


    else:
        return

if __name__ == '__main__':
    main()