from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import WellnessProgram, WellnessParticipation, Challenge, ChallengeParticipation
from datetime import datetime, timezone
import pytz

main = Blueprint('main', __name__)

def get_ist_time():
        ist = pytz.timezone("Asia/Kolkata")
        return datetime.now(ist)

@main.route("/adminpview")
def display_admin_wp():
    wplist = WellnessProgram.query.all()
    return render_template("adminprogramlist.html", programs=wplist)

@main.route('/addwp')
def create_wellness_program():
    return render_template("addprogram.html")

@main.route("/addwp", methods=['POST'])
def create_wp_post():
    pname = request.form["pname"]
    pstart = request.form["pstart"]
    pend = request.form["pend"]
    pvenue = request.form["pvenue"]
    porganizer = request.form['porganizer']
    pcategory = request.form['pcategory']
    pdesc = request.form['pdesc']
    pcontact = request.form['pcontact']

    print(pname, pstart, pend)

    pstart = datetime.strptime(pstart, '%Y-%m-%dT%H:%M')
    pstart = pstart.replace(tzinfo=timezone.utc)

    pend = datetime.strptime(pend, '%Y-%m-%dT%H:%M')
    pend = pend.replace(tzinfo=timezone.utc)

    wp = WellnessProgram(pname=pname, pstart=pstart, pend=pend,
                         pvenue=pvenue, porganizer=porganizer, 
                         pdesc=pdesc, pcontact=pcontact, pcategory=pcategory
                         )
    db.session.add(wp)
    db.session.commit()

    flash("new wellness program is added")

    return redirect(url_for("main.display_admin_wp"))

@main.route("/updatewp/<int:wpid>", methods=['GET', 'POST'])
def update_wp(wpid):
    wp = WellnessProgram.query.get_or_404(wpid)
    print(wp.pid, wp.pname, wp.pdesc)

    if request.method == "POST":
        wp.pname = request.form["pname"]
        wp.pvenue = request.form["pvenue"]
        wp.porganizer = request.form['porganizer']
        wp.pdesc = request.form['pdesc']
        wp.pcontact = request.form['pcontact']
        wp.pcategory = request.form['pcategory']
        pstart = request.form['pstart']
        pend =request.form['pend']

        pstart = datetime.strptime(pstart, '%Y-%m-%dT%H:%M')
        pstart = pstart.replace(tzinfo=timezone.utc)

        pend = datetime.strptime(pend, '%Y-%m-%dT%H:%M')
        pend = pend.replace(tzinfo=timezone.utc)

        wp.pstart = pstart
        wp.pend = pend

        db.session.commit()
        flash("Program details updated successfully")

        return redirect(url_for("main.display_admin_wp"))

    print("hello")
    return render_template("updateprogram.html", program=wp)

@main.route("/deletewp/<int:wpid>", methods=['GET', 'POST'])
def delete_wp(wpid):
    wp = WellnessProgram.query.get_or_404(wpid)
    db.session.delete(wp)
    db.session.commit()
    return redirect(url_for("main.display_admin_wp"))

## -----------------------------------------------------CHALLENGE FUNCTIONALITY ---------------------------------------

@main.route("/adminchview")
def display_admin_ch():
    chlist = Challenge.query.all()
    return render_template("adminchallengelist.html", challenges=chlist)

@main.route('/addch')
def create_challenge():
    return render_template("addchallenge.html")

@main.route("/addch", methods=['POST'])
def create_ch_post():
    chname = request.form["chname"]
    chstart = request.form["chstart"]
    chend = request.form["chend"]
    chvenue = request.form["chvenue"]
    chorganizer = request.form['chorganizer']
    chcategory = request.form['chcategory']
    chdesc = request.form['chdesc']
    chcontact = request.form['chcontact']
    chpoints = int(request.form['chpoints'])
    

    print(chname, chstart, chend)

    chstart = datetime.strptime(chstart, '%Y-%m-%dT%H:%M')
    chstart = chstart.replace(tzinfo=timezone.utc)

    chend = datetime.strptime(chend, '%Y-%m-%dT%H:%M')
    chend = chend.replace(tzinfo=timezone.utc)

    challenge = Challenge(chname=chname, chstart=chstart, chend=chend,
                         chvenue=chvenue, chorganizer=chorganizer, chpoints=chpoints,
                         chdesc=chdesc, chcontact=chcontact, chcategory=chcategory
                         )
    db.session.add(challenge)
    db.session.commit()

    flash("new challenge is added")

    return redirect(url_for("main.display_admin_ch"))

@main.route("/updatech/<int:chid>", methods=['GET', 'POST'])
def update_ch(chid):
    ch = Challenge.query.get_or_404(chid)
    print(ch.chid, ch.chname, ch.chdesc)

    if request.method == "POST":
        ch.chname = request.form["chname"]
        ch.chvenue = request.form["chvenue"]
        ch.chorganizer = request.form['chorganizer']
        ch.chdesc = request.form['chdesc']
        ch.chcontact = request.form['chcontact']
        ch.chpoints = int(request.form['chpoints'])
        ch.chcategory = request.form['chcategory']
        chstart = request.form['chstart']
        chend =request.form['chend']

        chstart = datetime.strptime(chstart, '%Y-%m-%dT%H:%M')
        chstart = chstart.replace(tzinfo=timezone.utc)

        chend = datetime.strptime(chend, '%Y-%m-%dT%H:%M')
        chend = chend.replace(tzinfo=timezone.utc)

        ch.chstart = chstart
        ch.chend = chend

        db.session.commit()
        flash("Challenge details updated successfully")

        return redirect(url_for("main.display_admin_ch"))

    print("hello")
    return render_template("updatechallenge.html", challenge=ch)

@main.route("/deletech/<int:chid>", methods=['GET', 'POST'])
def delete_ch(chid):
    challenge = Challenge.query.get_or_404(chid)
    db.session.delete(challenge)
    db.session.commit()
    return redirect(url_for("main.display_admin_ch"))




"""
=================================================================================
            ADMIN RELATED PROGRAMS FUNCTIONALITY ENDS HERE
            USER PROGRAMS RELATED FUNCTIONALITY STARTS FROM HERE 
=================================================================================
"""

@main.route("/userpview")
def display_user_wp():
    wplist = WellnessProgram.query.all()
    return render_template("userprogramlist.html", programs=wplist)

@main.route("/registerwp/<int:wpid>", methods=['GET', 'POST'])
def register_wp(wpid):
    userid = 1
    status = 'REGISTERED'
    pregtime = get_ist_time()
    wparticipation = WellnessParticipation(pid=wpid, uid=userid, pregtime=pregtime, status=status)
    db.session.add(wparticipation)
    db.session.commit()
    flash("Succesfully registered for the wellness program")
    return redirect(url_for("auth.userHome"))

@main.route("/userchview")
def display_user_ch():
    chlist = Challenge.query.all()
    return render_template("userchallengelist.html", challenges=chlist)

@main.route("/registerch/<int:chid>", methods=['GET', 'POST'])
def register_ch(chid):
    userid = 1
    status = 'REGISTERED'
    chregtime = get_ist_time()
    chparticipation = ChallengeParticipation(chid=chid, uid=userid, chregtime=chregtime, status=status)
    db.session.add(chparticipation)
    db.session.commit()
    flash("Succesfully registered for the challenge")
    return redirect(url_for("auth.userHome"))



"""
=================================================================================
            USER PROGRAMS FUNCTIONALITY ENDS HERE
            ADMIN PROGRAM PARTICIPATION FUNCTIONALITY STARTS FROM HERE 
=================================================================================
"""

@main.route("/wpparticipants<int:wpid>", methods=['POST', 'GET'])
def get_program_participations(wpid):
    wp = WellnessProgram.query.get_or_404(wpid)
    if wp is None:
        flash("Invalid wellness program id")
        return redirect(url_for("auth.adminHome"))
    programname = wp.pname
    participations = WellnessParticipation.query.filter_by(pid=wpid)
    return render_template("programparticipants.html", participations=participations, pname=programname)

@main.route("/chparticipants<int:chid>", methods=['POST', 'GET'])
def get_challenge_participations(chid):
    challenge = Challenge.query.get_or_404(chid)
    if challenge is None:
        flash("Invalid wellness program id")
        return redirect(url_for("auth.adminHome"))
    chname = challenge.chname
    challenges = ChallengeParticipation.query.filter_by(chid=chid)
    return render_template("challengeparticipants.html", challenges=challenges, chname=chname)




    




