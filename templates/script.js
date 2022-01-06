const getItems = () => {
  fetch("http://localhost:8000/api/items/")
    .then((res) => res.json())
    .then((res) => {
      let table = '<table class="mx-auto" border="3">';
      table += `<tr><th>ID</th><th>Name</th><th>Description</th><th>Price</th><th>Quantity</th></tr>`;

      res.forEach((element) => {
        table = table + `<tr>`;
        table = table + `<td> ${element.ItemID}</td>`;
        table = table + `<td> ${element.ItemName}</td>`;
        table = table + `<td> ${element.ItemDescription}</td>`;
        table = table + `<td>$ ${element.ItemPrice}</td>`;
        table = table + `<td> ${element.ItemQuantity}</td>`;
        table += `</tr>`;
      });
      table += "</table>";
      document.getElementById("list").innerHTML = table;
    });
};

function createItem() {
  const item = {
    ItemName: document.getElementById("ItemNameText").value,
    ItemQuantity: document.getElementById("ItemQuantNum").value,
    ItemPrice: document.getElementById("ItemPriceNum").value,
    ItemDescription: document.getElementById("ItemDescText").value,
  };
  fetch("http://localhost:8000/api/items/create/", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(item),
  })
    .then((response) => response.json())
    .then((res) => console.log(res));
}

const getItemDetails = () => {
  const itemId = document.getElementById("ItemNum").value;

  if (isNaN(itemId) || itemId === "") {
    alert("Enter a valid number!");
  } else {
    fetch(`http://localhost:8000/api/items/${itemId}`, {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((res) => {
        document.getElementById("UpdDelDiv").innerHTML = `<div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label">Name</label>
        <input type="text" class="form-control" id="ItemName" onchange="updateData('ItemName', this.value)" value='${res.ItemName}'>
    </div>
    <div class="mb-3">
        <label for="exampleFormControlTextarea1" class="form-label">Description</label>
        <input type="text" class="form-control" id="ItemDescription" onchange="updateData('ItemDescription', this.value)" value='${res.ItemDescription}' rows="3"></input>
    </div>
    <div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label">Price</label>
        <input type="number" class="form-control" id="ItemPrice" onchange="updateData('ItemPrice', this.value)" value='${res.ItemPrice}'>
    </div>
    <div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label">Quantity</label>
        <input type="number" class="form-control" id="ItemQuantity" onchange="updateData('ItemQuantity', this.value)" value='${res.ItemQuantity}'>
    </div>`;
      });
    document.getElementById("updateBtn").hidden = false;
    document.getElementById("deleteBtn").hidden = false;
  }
};

const updatedData = {};

const updateData = (id, value) => {
  updatedData[id] = value;
};

const updateItem = () => {
  if (Object.keys(updatedData).length === 0) {
    alert("Please edit some information!");
  } else {
    fetch(
      `http://localhost:8000/api/items/${
        document.getElementById("ItemNum").value
      }`,
      {
        method: "PATCH",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(updatedData),
      }
    )
      .then((res) => res.json())
      .then((response) => {
        alert("Information was updated!");
      });
  }
};

const deleteItem = () => {
  fetch(
    `http://localhost:8000/api/items/${
      document.getElementById("ItemNum").value
    }`,
    {
      method: "DELETE",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    }
  )
    .then((res) => res.json())
    .then((response) => {
      alert("Item was deleted");
    });
};
