'use strict';
(() => {
  // Calculate the sum of total votes
  const meters = document.getElementsByClassName('poll-meter');
  var totalVotes = 0;
  for (let meter of meters) {
    totalVotes += +meter.dataset.votes;
  };
  // Set proportional poll-meter widths by score
  // NOTE: CSS transitions in Chrome only work when executed async
  setTimeout(() => {
    for (let meter of meters) {
      const width = +meter.dataset.votes / totalVotes * 100;
      meter.style.width = width + '%';
    };
  }, 0);
})();
