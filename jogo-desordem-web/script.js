function countInversionsVerbose(arr) {
  const steps = [];

  function mergeSort(arr) {
    if (arr.length <= 1) return { sorted: arr, inversions: 0 };

    const mid = Math.floor(arr.length / 2);
    const left = arr.slice(0, mid);
    const right = arr.slice(mid);

    steps.push(`📎 Dividindo: [${left.join(" ")}] e [${right.join(" ")}]`);

    const leftResult = mergeSort(left);
    const rightResult = mergeSort(right);
    const merged = merge(leftResult.sorted, rightResult.sorted);

    const totalInv = leftResult.inversions + rightResult.inversions + merged.inversions;

    steps.push(`📎 Juntando: [${merged.sorted.join(" ")}] (${merged.inversions} inversões)`);

    return { sorted: merged.sorted, inversions: totalInv };
  }

  function merge(left, right) {
    let result = [], i = 0, j = 0, invCount = 0;

    while (i < left.length && j < right.length) {
      if (left[i] <= right[j]) {
        result.push(left[i++]);
      } else {
        result.push(right[j++]);
        invCount += left.length - i;
      }
    }

    result = result.concat(left.slice(i)).concat(right.slice(j));
    return { sorted: result, inversions: invCount };
  }

  const final = mergeSort(arr);
  steps.push(`📢 Total de inversões: ${final.inversions}`);
  return { inversions: final.inversions, steps: steps };
}

function checkAnswer() {
  const input = document.getElementById("userInput").value.trim();
  const userList = input.split(" ").map(Number);
  const resultDiv = document.getElementById("result");
  const stepsDiv = document.getElementById("steps");

  if (userList.some(isNaN)) {
    resultDiv.innerText = "❌ Por favor, digite apenas números separados por espaço.";
    stepsDiv.innerText = "";
    return;
  }

  const { inversions, steps } = countInversionsVerbose(userList);

  let message = `✅ Sua lista tem ${inversions} inversões.\n`;
  if (inversions === 0) {
    message += "🏆 A lista está perfeitamente ordenada!";
  } else {
    message += "📊 Veja abaixo as divisões e contagens:";
  }

  resultDiv.innerText = message;
  stepsDiv.innerText = steps.join("\n");
}
