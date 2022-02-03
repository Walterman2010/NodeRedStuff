# NodeRedStuff
This is more for me and my personal Documentation, but please feel free to use it pirvate. Some Prate ist just Copy and Paste, I always try to add the source. But I think comerzial use ist difficult...

________________________________________________________________________________
OPC-UA_ServerClientReadWrite 

  it create a Server and write and read Values
  It can happen, that the variable create not work automaticly, than you have to press the following inject after every deploy
  1. add fulder
  2. add Variable
  3. write Variable

  Source:   https://www.automation.siemens.com/sce-static/learning-training-documents/tia-portal/advanced-communication/sce-092-303-opc-ua-s7-1500-node-red-de.pdf
            https://support.elsist.biz/de/articoli/opc-ua-client-con-node-red/
![grafik](https://user-images.githubusercontent.com/23342140/152413539-e4f8f22c-6507-4c85-ab85-b28116353207.png)
________________________________________________________________________________
CalcTimeDifferent

  this calculate the Timedifferent bettween to timestamps.
   1. the time Stamp will send, with the delay by mqtt.
   2. the mqtt timestamp and the aktual timestamp will be subtrahiert
   3. the difference will shown on the dashbord
  
 ![grafik](https://user-images.githubusercontent.com/23342140/152413167-dfb2bfef-1b0b-4fc3-88b8-afe417a15197.png)

________________________________________________________________________________
RCswitch 

  this tool can controll romote Power Plugs (Funksteckdosen), based on 433/315MHz Chips. For using that tool ist my Node Red installed on a Raspberry Pi and the RC chips are wired to the Pi. 
  The Flow is nothing else, than a call a Phython Programm, where we say the Programm, witch Power Plug get switch. the Phyton Programm is called "rcs-sender.py" and you can find it in Git as well or in the comment "rcs-sender.py code". Before you can send the Power On/off Command, you need to figger out how the command is called. For that you will need a reseave chip an the Python toll "rcs-empfang.py". That you also can fing in the command.
![grafik](https://user-images.githubusercontent.com/23342140/152432519-21447b68-3c44-4a0e-8dcb-1615df8728dd.png)
________________________________________________________________________________
AVR_Net_IO_controll

this Tool is not working jet!
its try to controll the AVR Net IO. It just not Workin well, hat never time for Debug jet.

![grafik](https://user-images.githubusercontent.com/23342140/152435019-653f5619-1991-47fb-b845-66f51c54e8aa.png)
________________________________________________________________________________
Good_Morning_Alarm

It was not my creation. the creation by Mat Zolnierczyk was just not working. so i did some smal changes in the Day selection and is was working fine. I connected the Alarm to the RCs, to turn on a light to wake me up

Surce:  https://flows.nodered.org/flow/f24cb20846f57eec19ed617b25cb61ae
        https://flows.nodered.org/flow/7e4bb517ce3a75add0083642ef03e9d8
        
![grafik](https://user-images.githubusercontent.com/23342140/152436354-179dbada-7a3f-4588-96dd-9acf12042e53.png)
