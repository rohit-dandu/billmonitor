var index = 0;

// The invoker class
class Button {
    constructor() {
        this._commands = [];
    }

    storeAndExecute(command) {
        this._commands.push(command);
        command.execute();
    }
}

// The receiver class
class Toolbar {
    addItem() {
        index++;
        const tr = document.createElement('tr');
        tr.id = "'row"+index+"'";
      
        tr.innerHTML = "<td><input name='name"+index+"' type='text' class='form-input name'/></td><td><select name='cat"+index+"' class='form-input cat'><option value='gro'>Grocery</option><option value='sna'>Snack</option><option value='ute'>Utensils</option><option selected value='oth'>Other</option></select></td><td><input name='qty"+index+"' type='number' class='form-input qty' oninput='calculate()'></td><td><input name='price"+index+"' type='number' step='.01' class='form-input price' oninput='calculate()'></td>";
        document.getElementById('item-table').appendChild(tr);
        calculate();
    }

    removeItem() {
        if(index >= 1) {
            document.getElementById('item-table').deleteRow(-1);
            index--;
        }
    }
}

// Command object knows about the receiver and invokes the methods
// of the receiver.

// Command for adding a row item
class AddItemCommand {
    constructor(toolbar) {
        this._toolbar = toolbar;
    }

    execute() {
        this._toolbar.addItem();
    }
}

// Command for removing a row item
class RemoveItemCommand {
    constructor(toolbar) {
        this._toolbar = toolbar;
    }

    execute() {
        this._toolbar.removeItem();
    }
}

// Client functions
function addItem() {
    var toolbar = new Toolbar();
    var addI = new AddItemCommand(toolbar);
    var button = new Button();

    button.storeAndExecute(addI);
}

function removeItem() {
    var toolbar = new Toolbar();
    var removeI = new RemoveItemCommand(toolbar);
    var button = new Button();

    button.storeAndExecute(removeI);
}

function calculate() {
    var total = 0;
    priceList = document.getElementsByClassName("price");
    qtyList = document.getElementsByClassName("qty");

    for (var i = 0; i < priceList.length; i++) {
        total += qtyList[i].value * priceList[i].value;
    }
    document.getElementById("total").value = Math.round((total + Number.EPSILON) * 100) / 100;
}