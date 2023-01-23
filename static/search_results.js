var ctx = document.getElementById('price-chart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Price',
            data: [],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

function updateChart() {
    $.get("/search_results", function(short_details) {
        chart.data.labels = short_details.timestamp;
        chart.data.datasets[0].data = short_details.price;
        chart.update();
    });
}

setInterval(updateChart, 3000);
