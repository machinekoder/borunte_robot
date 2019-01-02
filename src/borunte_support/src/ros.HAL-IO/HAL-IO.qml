import QtQuick 2.0
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1
import Machinekit.Controls 1.0
import Machinekit.HalRemote.Controls 1.0
import Machinekit.HalRemote 1.0

HalApplicationWindow {
  id: main

  name: "io-rcomp"
  title: qsTr("HAL-IO")

  ColumnLayout {
    anchors.fill: parent
    anchors.margins: 10

    Item {
      Layout.fillHeight: true
    }
    HalButton {
      Layout.alignment: Layout.Center
      name: "digital_in_1"
      text: "Digital In 1"
      checkable: true
    }
    HalButton {
      Layout.alignment: Layout.Center
      name: "digital_in_2"
      text: "Digital In 2"
      checkable: true
    }
    HalButton {
      Layout.alignment: Layout.Center
      name: "digital_in_3"
      text: "Digital In 3"
      checkable: true
    }
    HalButton {
      Layout.alignment: Layout.Center
      name: "digital_in_4"
      text: "Digital In 4"
      checkable: true
    }

    RowLayout {
      Layout.alignment: Layout.Center
      Label {
        text: "Digital Out 1: "
      }
      HalLed {
        name: "digital_out_1"
      }
    }
    RowLayout {
      Layout.alignment: Layout.Center
      Label {
        text: "Digital Out 2: "
      }
      HalLed {
        name: "digital_out_2"
      }
    }
    RowLayout {
      Layout.alignment: Layout.Center
      Label {
        text: "Digital Out 3: "
      }
      HalLed {
        name: "digital_out_3"
      }
    }
    RowLayout {
      Layout.alignment: Layout.Center
      Label {
        text: "Digital Out 4: "
      }
      HalLed {
        name: "digital_out_4"
      }
    }

    Item {
      Layout.fillHeight: true
    }
  }
}
