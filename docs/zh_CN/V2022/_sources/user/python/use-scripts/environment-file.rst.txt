==================================================================
Using Abaqus Scripting Interface commands in your environment file
==================================================================

The Abaqus environment file is read by Abaqus/CAE when you start a session. The environment file can contain Abaqus Scripting Interface commands. The following is an example environment file:

.. code-block:: python2

    scratch = 'c:/temp'
    memory = 256mb

    def onCaeGraphicsStartup():

        # Graphics preferences
        #
        session.defaultGraphicsOptions.setValues(
            displayLists=OFF, dragMode=AS_IS)

    def onCaeStartup():

        # Print preferences
        #
        session.printOptions.setValues(vpDecorations=OFF,
            vpBackground=OFF, rendition=COLOR,
            printCommand='lpr')
        session.psOptions.setValues(date=OFF)

        # Job preferences
        #
        def setJobPreferences(module, userData):
        
            import job
            session.Queue(name='long', hostName='server',
                queueName='large', directory='/tmp')
        addImportCallback('job', setJobPreferences)

        # Visualization preferences
        #
        def setVisPreferences(module, userData):
        
            import visualization
            session.defaultOdbDisplay.contourOptions.setValues(
                renderStyle=SHADED, visibleEdges=EXTERIOR,
                contourStyle=CONTINUOUS)
        addImportCallback('visualization', setVisPreferences)

The `addImportCallback` statement instructs Abaqus to call a function when the user first imports a module. In this example Abaqus calls the `setJobPreferences` function when the user first enters the Job module, and Abaqus calls the `setVisPreferences` function when the user first enters the Visualization module. The `setJobPreferences` function creates a queue on a remote host. The `setVisPreferences` function sets default options for contour plots.

The example environment file uses the `onCaeStartup()` function to control a set of Python statements that are executed when Abaqus/CAE first starts. The environment file can also contain the following:

- The `onJobStartup()` function controls a set of statements that execute when an analysis job starts. For example,

  .. code-block:: python2

      def onJobStartup():
          import os, shutil
          restartDir = savedir + id + '_restart'
          if (os.path.exists(restartDir)):
              shutil.rmtree(restartDir)

- The onJobCompletion() function controls a set of statements that execute when an analysis job completes. For example,

  .. code-block:: python2

      def onJobCompletion():
          import os
          extensions = ('res','stt','mdl','prt','abq','pac')
          restartDir = savedir + os.sep + id + '_restart'
          if (not os.path.exists(restartDir)):
              os.mkdir(restartDir)
          for extension in extensions:
              fileName = id + '.' + extension
              if (os.path.exists(savedir + os.sep + fileName)):
                  os.rename(savedir + os.sep + fileName, 
                      restartDir + os.sep + fileName)

The following variables are available to the `onJobStartup()` and `onJobCompletion()` functions:

- **id**

  The job identifier that was specified as the value of the job option from the command line.

- **savedir**

  The path to the directory from which the job was submitted.

- **scrdir**

  The path to the scratch directory.

- **analysisType**

  The type of analysis to be executed. Possible values are STANDARD and EXPLICIT.

For a list of the variables that are available outside of the `onJobStartup()` and `onJobCompletion()` functions, see Job variables.

For more information on the environment file, see `Environment File Settings <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEEXCRefMap/simaexc-c-envfile.htm?contextscope=all>`_ and `Customizing the Abaqus environment <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEILGRefMap/simailg-m-Environment-sb.htm?contextscope=all>`_. 