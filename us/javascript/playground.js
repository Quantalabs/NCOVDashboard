function generate () {
    project = document.getElementById('project')
    project.style['display'] = 'block'
    document.getElementById('output').remove()
    document.getElementById('cantsee').remove()
    output = document.createElement("canvas")
    output.id = "output"
    document.getElementById('Projection').appendChild(output)
    document.getElementById('Projection').innerHTML += '<p id="cantsee">Can\'t see anything? Try and switch browsers or reload.</p>'

    i = Number(document.getElementById('i').value) 
    rn = Number(document.getElementById('r').value)
    rr = Number(document.getElementById('rr').value)
    s = Number(document.getElementById('s').value)
    inc = Number(document.getElementById('inc').value)
    recov = Number(document.getElementById('recov').value)
    pop = s+i+recov

    // seir("output", 4, 9900, 1, 100, 1/7, 1/7, 10000)
    seir("output", rn, s, i, 365, rr, 1/inc, pop)
}